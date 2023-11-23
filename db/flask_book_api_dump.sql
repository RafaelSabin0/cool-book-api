/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- DB name: `flask_book_api`
--

-- --------------------------------------------------------

CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Sample data for the books table
--

INSERT INTO `books` (`id`, `title`, `author`, `price`) VALUES
(1, 'Journey to the center of the earth', 'Jules Verne', 3.00),
(2, 'Sherlock Holmes', 'Arthur Conan Doyle', 31.00),
(3, 'Jungle Book', 'Rudyard Kipling', 10.00),
(4, 'Death on the Nile', 'Agatha Christie', 30.99),
(5, 'Pride and Prejudice', 'Jane Austen', 15.55),
(6, 'Sense and Sensibility', 'Jane Austen', 15.55);


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
