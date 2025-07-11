-- 3570. Find Books with No Available Copies

SELECT
    `library_books`.book_id,
    title,
    author,
    genre,
    publication_year,
    total_copies AS current_borrowers
FROM
    `library_books`
    JOIN (
        SELECT
            book_id,
            COUNT(record_id) AS copies
        FROM
            borrowing_records
        WHERE
            return_date IS NULL
        GROUP BY
            book_id
    ) AS `TBL` ON `library_books`.book_id = `TBL`.book_id
    AND `library_books`.total_copies = `TBL`.copies
ORDER BY
    current_borrowers DESC,
    title ASC;
