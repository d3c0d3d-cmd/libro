from PyQt5.QtSql import QSqlQuery

import os
import shutil

from datetime import date
from enum import Enum

import libro.queries as queries
import libro.config as config
import libro.ebookmeta as ebookmeta
import libro.utils.util as util


class BookRec:

    __slots__ = ['id', 'title', 'author', 'author_sort', 'series', 'series_index',
                 'tags', 'type', 'lang', 'translator', 'date_added',
                 'cover_image', 'file']


class Collection:
    def __init__(self, id=None, type=None, name=None, criteria=None):
        self.id = id
        self.type = type
        self.name = name
        self.criteria = criteria


class CollectionType(Enum):
    System = 0
    Collection = 1
    Smart = 2


class SystemCollectionId(Enum):
    AllBooks = -1
    AddedToday = -2
    AddedLastWeek = -3


def get_collection_list(collection_type=None):
    collection_list = []
    q = QSqlQuery(config.db)
    if collection_type is None:
        q.exec(queries.GET_COLLECTION_LIST)
    else:
        q.prepare(queries.GET_COLLECTION_LIST_TYPE)
        q.bindValue(0, collection_type.value)
        q.exec_()

    while q.next():
        collection = Collection()
        collection.id = q.value(0)
        collection.name = q.value(1)
        collection.type = CollectionType(q.value(2))
        collection.criteria = q.value(3)
        collection_list.append(collection)
    return collection_list


def get_book_collection_list(book_id):
    collection_list = []
    q = QSqlQuery(config.db)
    q.prepare(queries.GET_BOOK_COLLECTIONS)
    q.bindValue(0, book_id)
    q.exec_()

    while q.next():
        collection = Collection()
        collection.id = q.value(0)
        collection.name = q.value(1)
        collection.type = CollectionType.Collection
        collection.criteria = ''
        collection_list.append(collection)
    return collection_list


def add_book_in_collection(book_id, collection):
    err = ''
    q = QSqlQuery(config.db)
    q.prepare(queries.ADD_BOOK_IN_COLLECTION)
    q.bindValue(0, collection.id)
    q.bindValue(1, book_id)
    if not q.exec_():
        err = q.lastError().text()
        config.db.rollback()
    else:
        config.db.commit()
    return err


def remove_book_from_collection(book_id, collection):
    err = ''
    q = QSqlQuery(config.db)
    q.prepare(queries.DELETE_BOOK_FROM_COLLECTION)
    q.bindValue(0, collection.id)
    q.bindValue(1, book_id)
    if not q.exec_():
        err = q.lastError().text()
        config.db.rollback()
    else:
        config.db.commit()
    return err


def create_collection(collection):
    err = ''
    q = QSqlQuery(config.db)
    q.prepare(queries.CREATE_COLLECTION)
    q.bindValue(0, collection.name)
    q.bindValue(1, collection.type.value)
    q.bindValue(2, collection.criteria)
    if not q.exec_():
        err = q.lastError().text()
        config.db.rollback()
    else:
        collection.id = q.lastInsertId()
        config.db.commit()
    return collection, err


def update_collection(collection):
    err = ''
    q = QSqlQuery(config.db)
    q.prepare(queries.UPDATE_COLLECTION)
    q.bindValue(0, collection.name)
    q.bindValue(1, collection.type.value)
    q.bindValue(2, collection.criteria)
    q.bindValue(3, collection.id)
    if not q.exec_():
        err = q.lastError().text()
        config.db.rollback()
    else:
        config.db.commit()
    return err


def delete_collection(collection):
    err = ''
    q = QSqlQuery(config.db)
    if collection.type == CollectionType.Collection:
        q.prepare(queries.DELETE_BOOKS_FROM_COLLECTION)
        q.bindValue(0, collection.id)
        if not q.exec_():
            err = q.lastError().text()
            config.db.rollback()

    if not err:
        q.prepare(queries.DELETE_COLLECTION)
        q.bindValue(0, collection.id)
        if not q.exec_():
            err = q.lastError().text()
            config.db.rollback()
        else:
            config.db.commit()
    return err


def get_book_info(id):

    q = QSqlQuery(config.db)
    q.prepare(queries.SELECT_BOOK_INFO)
    q.bindValue(0, id)
    q.exec_()
    if q.next():
        file = q.value(0)
        meta = ebookmeta.get_metadata(file)
        meta.id = id
        return meta
    else:
        return None


def get_book_rec(id):

    q = QSqlQuery(config.db)
    q.prepare(queries.SELECT_BOOK_REC)
    q.bindValue(0, id)
    q.exec_()
    if q.next():
        b = BookRec()
        b.id = q.value(0)
        b.title = q.value(1)
        b.author = q.value(2)
        b.author_sort = q.value(3)
        b.series = q.value(4)
        b.tags = q.value(5)
        b.lang = q.value(6)
        b.translator = q.value(7)
        b.type = q.value(8)
        b.date_added = q.value(9)
        b.file = q.value(10)

        return b
    else:
        return BookRec()


def update_book_info(book_meta):

    ebookmeta.set_metadata(book_meta.file, book_meta)
    q = QSqlQuery(config.db)
    q.prepare(queries.UPDATE_BOOK)
    q.bindValue(0, book_meta.title)
    q.bindValue(1, book_meta.get_author_string())
    q.bindValue(2, book_meta.get_author_sort_string())
    q.bindValue(3, book_meta.get_tag_description_string())
    q.bindValue(4, book_meta.series)
    q.bindValue(5, book_meta.series_index)
    q.bindValue(6, book_meta.lang)
    q.bindValue(7, book_meta.get_translator_string())
    q.bindValue(8, book_meta.format)
    q.bindValue(9, book_meta.id)
    if not q.exec_():
        print(q.lastError().text())
        config.db.rollback()
    else:
        config.db.commit()


def delete_book(id):

    q = QSqlQuery(config.db)
    q.prepare(queries.DELETE_BOOK)
    q.bindValue(0, id)
    if not q.exec_():
        print(q.lastError().text())
        config.db.rollback()
    else:
        config.db.commit()


def add_book(file):

    src = ''
    err = []

    file = os.path.normpath(file)
    src = file

    try:
        meta = ebookmeta.get_metadata(file)
        cur_date = date.today().strftime('%d.%m.%Y')
        if config.collect_files:
            file = move_to_library(file, meta)

        q = QSqlQuery(config.db)
        q.prepare(queries.INSERT_BOOK)
        q.bindValue(0, meta.title)
        q.bindValue(1, meta.get_author_string())
        q.bindValue(2, meta.get_author_sort_string())
        q.bindValue(3, meta.get_tag_description_string())
        q.bindValue(4, meta.series)
        q.bindValue(5, meta.series_index)
        q.bindValue(6, meta.lang)
        q.bindValue(7, meta.get_translator_string())
        q.bindValue(8, meta.format)
        q.bindValue(9, cur_date)
        q.bindValue(10, file)
        if not q.exec_():
            err_text = q.lastError().text()
            err.append(('ERROR', err_text))
            config.db.rollback()
        else:
            config.db.commit()
    except Exception as e:
        err_text = '{}'.format(e)
        err.append(('ERROR', err_text))

    return src, err

def move_to_library(file, meta):
    title = meta.get_title_for_filename()
    author = meta.get_author_for_filename()
    series = meta.get_series_for_filename()
    series_num = meta.get_series_index_for_filename()
    translator = meta.get_translator_for_filename()

    dest_name = util.format_pattern(config.filename_pattern,
        [
            ('#title', title),
            ('#author', author),
            ('#series', series),
            ('#number', series_num),
            ('#translator', translator)
        ])
    if file.lower().endswith('fb2.zip'):
        file_ext = '.fb2.zip'
    else:
        file_ext = os.path.splitext(file)[1]
    dest_file = os.path.normpath(os.path.join(config.library_root_path, dest_name + file_ext))
    if not os.path.exists(dest_file):
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        shutil.copy(file, dest_file)
    else:
        raise Exception('File already exists {}'.format(dest_file))

    return dest_file


def is_created():

    rows = -1
    q = QSqlQuery(config.db)
    q.exec(queries.CHECK_DB_CREATED)
    if q.next():
        rows = q.value(0)

    return rows == 1


def create():

    q = QSqlQuery(config.db)
    sql_lines = queries.CREATE_DB.split(';')
    for sql_line in sql_lines:
        if len(sql_line.strip()) > 0:
            if not q.exec(sql_line):
                print(q.lastError().text())

    if not q.exec(queries.TRIGGER_AI):
        print(q.lastError().text())
    if not q.exec(queries.TRIGGER_AD):
        print(q.lastError().text())
    if not q.exec(queries.TRIGGER_AU):
        print(q.lastError().text())


def update():

    if not check_table_exist('collection'):
        errors = execute_script(queries.CREATE_COLLECTIONS)
        if len(errors) > 0:
            print(errors)


def execute_script(script):

    errors = []
    q = QSqlQuery(config.db)
    sql_lines = script.split(';')
    for sql_line in sql_lines:
        if len(sql_line.strip()) > 0:
            if not q.exec(sql_line):
                errors.append(q.lastError().text())

    return errors


def check_table_exist(table_name):

    rows = -1
    q = QSqlQuery(config.db)
    q.prepare(queries.CHECK_TABLE_EXISTS)
    q.bindValue(0, table_name)
    q.exec_()
    if q.next():
        rows = q.value(0)

    return rows == 1
