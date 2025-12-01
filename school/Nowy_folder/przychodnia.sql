-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Paź 29, 2025 at 08:48 PM
-- Wersja serwera: 10.4.32-MariaDB
-- Wersja PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `przychodnia`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lekarze`
--

CREATE TABLE `lekarze` (
  `Id_lek` int(11) NOT NULL,
  `Pesel` varchar(11) NOT NULL,
  `Imie` text NOT NULL,
  `Nazwisko` text NOT NULL,
  `Telefon` varchar(9) NOT NULL,
  `Specjalnosc` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `lekarze`
--

INSERT INTO `lekarze` (`Id_lek`, `Pesel`, `Imie`, `Nazwisko`, `Telefon`, `Specjalnosc`) VALUES
(1, '01963810582', 'Michał', 'Srebrny', '892375014', 'Kardiolog'),
(2, '53091628403', 'Aneta', 'Woźniak', '887294606', 'Chirurg'),
(3, '63722093748', 'Marcel', 'Kwiat', '992675431', 'Dentysta'),
(4, '61904388528', 'Bolesława', 'Martyniuk', '162873009', 'Fizjoterapeuta'),
(5, '77456290043', 'Piotr', 'Gaja', '723884561', 'Chirurg');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pacjenci`
--

CREATE TABLE `pacjenci` (
  `Id_pac` int(11) NOT NULL,
  `Pesel` varchar(11) NOT NULL,
  `Imie` text NOT NULL,
  `Nazwisko` text NOT NULL,
  `Telefon` varchar(9) NOT NULL,
  `data_ur_pac` date DEFAULT NULL,
  `miasto_zam` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `pacjenci`
--

INSERT INTO `pacjenci` (`Id_pac`, `Pesel`, `Imie`, `Nazwisko`, `Telefon`, `data_ur_pac`, `miasto_zam`) VALUES
(1, '78324081644', 'Antoni', 'Wiśniewski', '834678543', '1967-12-09', 'Opole'),
(2, '73451956923', 'Martyna', 'Sowa', '846472237', '1988-03-23', 'Częstochowa'),
(3, '35756582365', 'Katarzyna', 'Migdał', '953763429', '2001-07-16', 'Kadłub'),
(4, '54322765289', 'Dominik', 'Plac', '832563205', '1978-04-30', 'Opole'),
(5, '12098546254', 'Paulina', 'Łuk', '612453329', '2004-06-22', 'Zawadzkie');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wizyty`
--

CREATE TABLE `wizyty` (
  `Id_wizyty` int(11) NOT NULL,
  `data_wizyty` date NOT NULL,
  `Pesel_lek` varchar(11) NOT NULL,
  `Pesel_pac` varchar(11) NOT NULL,
  `id_zal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `wizyty`
--

INSERT INTO `wizyty` (`Id_wizyty`, `data_wizyty`, `Pesel_lek`, `Pesel_pac`, `id_zal`) VALUES
(1, '2023-12-07', '01963810582', '73451956923', 3),
(2, '2025-03-21', '53091628403', '54322765289', 1),
(3, '2024-09-26', '61904388528', '5348906621', 6),
(4, '2025-07-14', '77456290043', '78324081644', 4);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zalecenia`
--

CREATE TABLE `zalecenia` (
  `id_zalecen` int(11) NOT NULL,
  `rozpoznanie` text NOT NULL,
  `skierowanie` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `zalecenia`
--

INSERT INTO `zalecenia` (`id_zalecen`, `rozpoznanie`, `skierowanie`) VALUES
(1, 'Zapalenie stawu biodrowego', 1),
(2, 'Gorączka', 0),
(3, 'Cukrzyca', 1),
(4, 'Krwotok wewnetrzny', 1),
(5, 'Przeziębienie', 0),
(6, 'Kaszel', 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `lekarze`
--
ALTER TABLE `lekarze`
  ADD PRIMARY KEY (`Id_lek`);

--
-- Indeksy dla tabeli `pacjenci`
--
ALTER TABLE `pacjenci`
  ADD PRIMARY KEY (`Id_pac`);

--
-- Indeksy dla tabeli `wizyty`
--
ALTER TABLE `wizyty`
  ADD PRIMARY KEY (`Id_wizyty`);

--
-- Indeksy dla tabeli `zalecenia`
--
ALTER TABLE `zalecenia`
  ADD PRIMARY KEY (`id_zalecen`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lekarze`
--
ALTER TABLE `lekarze`
  MODIFY `Id_lek` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `pacjenci`
--
ALTER TABLE `pacjenci`
  MODIFY `Id_pac` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `wizyty`
--
ALTER TABLE `wizyty`
  MODIFY `Id_wizyty` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `zalecenia`
--
ALTER TABLE `zalecenia`
  MODIFY `id_zalecen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*CREATE USER IF NOT EXISTS 'operator_user'@'localhost' IDENTIFIED BY '';

GRANT `operator` TO 'operator_user'@'localhost';

SET DEFAULT ROLE `operator` TO 'operator_user'@'localhost';

REVOKE `operator` FROM 'operator_user'@'localhost';

DROP ROLE IF EXISTS 'operator';
*/;

