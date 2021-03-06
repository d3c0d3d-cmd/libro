
CREATE_DB = '''
    CREATE TABLE book (
        id integer PRIMARY KEY AUTOINCREMENT,
        title text NOT NULL,
        author text NOT NULL,
        author_sort text NOT NULL,
        tags text,
        series text,
        series_index integer,
        lang text,
        translator text,
        type text NOT NULL,
        date_added text NOT NULL,
        file text NOT NULL UNIQUE
    );

    CREATE VIEW v_book AS
    SELECT id,
           title,
           author,
           author_sort,
           case
              when length(series) > 0 and length(series_index) = 0 then
                   series
              when length(series) > 0 and length(series_index) > 0 then
                   series||' ('||series_index||')'
           end series,
           tags,
           lang,
           translator,
           type,
           date_added,
           file
      FROM book;

    CREATE INDEX idx_book_title ON book(title);
    CREATE INDEX idx_book_author ON book(author);
    CREATE INDEX idx_book_series ON book(series);

    CREATE VIRTUAL TABLE book_idx USING fts5(
        title,
        author,
        tags,
        series,
        lang,
        type,
        content = 'book',
        content_rowid = 'id'
    );
'''
TRIGGER_AI = '''
    CREATE TRIGGER book_ai AFTER INSERT ON book
    BEGIN
        INSERT INTO book_idx(rowid, title, author, tags, series, lang, type)
            VALUES(new.id, new.title, new.author, new.tags, new.series, new.lang, new.type);
    END;
'''
TRIGGER_AD = '''
    CREATE TRIGGER book_ad AFTER DELETE ON book
    BEGIN
        INSERT INTO book_idx(book_idx, rowid, title, author, tags, series, lang, type)
            VALUES('delete', old.id, old.title, old.author, old.tags, old.series, old.lang, old.type);
    END;
'''
TRIGGER_AU = '''
    CREATE TRIGGER book_au AFTER UPDATE ON book
    BEGIN
        INSERT INTO book_idx(book_idx, rowid, title, author, tags, series, lang, type)
            VALUES('delete', old.id, old.title, old.author, old.tags, old.series, old.lang, old.type);
        INSERT INTO book_idx(rowid, title, author, tags, series, lang, type)
            VALUES(new.id, new.title, new.author, new.tags, new.series, new.lang, new.type);
    END;
'''

CHECK_DB_CREATED = '''
  SELECT count(1) FROM sqlite_master WHERE type = "table" AND name = "book"
'''

INSERT_BOOK = '''
    INSERT INTO book (title, author, author_sort, tags, series, series_index, lang, translator, type, date_added, file)
       VALUES (?,?,?,?,?,?,?,?,?,?,?)
'''

UPDATE_BOOK = '''
    UPDATE book SET title=?, author=?, author_sort=?, tags=?, series=?, series_index=?,
                    lang=?, translator=?, type=?
     WHERE id = ?
'''

SELECT_BOOK = '''
    SELECT id,
           title,
           author,
           author_sort,
           case
              when length(series) > 0 and series_index is null then
                   series
              when length(series) > 0 and series_index is not null then
                   series||' ('||series_index||')'
           end series,
           tags,
           lang,
           type,
           date_added,
           file
      FROM book
'''

DELETE_BOOK = '''
 DELETE FROM book WHERE id = ?
'''

SELECT_BOOK_INFO = '''
    SELECT file
      FROM book
    WHERE id = ?
'''

SELECT_BOOK_REC = '''
    SELECT id,
           title,
           author,
           author_sort,
           series,
           tags,
           lang,
           translator,
           type,
           date_added,
           file
      FROM v_book
     WHERE id = ?
'''

CHECK_TABLE_EXISTS = '''
  SELECT count(1) FROM sqlite_master WHERE type = "table" AND name = ?
'''

CREATE_COLLECTIONS = '''
   CREATE TABLE collection (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        type integer,
        criteria text
    );

   CREATE TABLE collection_book (
        collection_id integer NOT NULL,
        book_id integer NOT NULL,
        PRIMARY KEY(collection_id, book_id),
        FOREIGN KEY(collection_id) REFERENCES collection(id),
        FOREIGN KEY(book_id) REFERENCES book(id)
    );

    CREATE INDEX idx_collection_book_id ON collection_book(collection_id);
'''

GET_COLLECTION_LIST = '''
  SELECT id, name, type, criteria FROM collection ORDER BY name
'''

GET_COLLECTION_LIST_TYPE = '''
  SELECT id, name, type, criteria FROM collection WHERE type=? ORDER BY name
'''

CREATE_COLLECTION = '''
  INSERT INTO collection (name, type, criteria) VALUES(?,?,?)
'''

UPDATE_COLLECTION = '''
  UPDATE collection  SET name=?, type=?, criteria=? WHERE id=?
'''

DELETE_COLLECTION = '''
  DELETE FROM collection  WHERE id=?
'''

DELETE_BOOKS_FROM_COLLECTION = '''
  DELETE FROM collection_book WHERE collection_id = ?
'''

GET_BOOK_COLLECTIONS = '''
    SELECT c.id, c.name
      FROM collection_book cb, collection c
     WHERE cb.collection_id = c.id
       AND cb.book_id = ?
'''

ADD_BOOK_IN_COLLECTION = '''
  INSERT INTO collection_book (collection_id, book_id) VALUES (?,?)
'''

DELETE_BOOK_FROM_COLLECTION = '''
  DELETE FROM collection_book  WHERE collection_id=? AND book_id=?
'''
