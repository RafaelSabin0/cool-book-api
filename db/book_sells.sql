CREATE TABLE `book_sells` (
  `id` int NOT NULL,
  `book_id` int NOT NULL,
  `quantity` int NOT NULL,
  `total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `book_sells` (`id`, `book_id`, `quantity`, `total`) VALUES
(1, 1, 10, NULL),
(2, 2, 15, NULL),
(3, 3, 144, NULL),
(4, 4, 90, NULL),
(5, 6, 68, NULL),
(6, 7, 54, NULL),
(7, 17, 28, NULL),
(8, 18, 35, NULL),
(9, 19, 198, NULL),
(10, 20, 83, NULL);


ALTER TABLE `book_sells`
  ADD UNIQUE KEY `id` (`id`);


ALTER TABLE `book_sells`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;
