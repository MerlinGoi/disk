CREATE TABLE `kategorie` (
  `id` int(11) NOT NULL,
  `nazwa` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `kategorie` (`id`, `nazwa`) VALUES
(1, 'Naprawy'),
(2, 'Edukacja'),
(3, 'Warsztaty');


CREATE TABLE `uslugi` (
  `id` int(11) NOT NULL,
  `tytul` varchar(255) NOT NULL,
  `opis` text NOT NULL,
  `data_dodania` datetime DEFAULT current_timestamp(),
  `kategoria_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `uslugi` (`id`, `tytul`, `opis`, `data_dodania`, `kategoria_id`) VALUES
(1, 'Naprawa komputerów', 'Oferuję szybkie i tanie naprawy komputerów.', '2025-11-01 10:00:00', 1),
(2, 'Korepetycje z języka angielskiego', 'Lekcje indywidualne dla dorosłych i młodzieży.', '2025-11-02 12:00:00', 2),
(3, 'Warsztaty stolarskie', 'Organizuję kursy stolarskie w weekendy.', '2025-11-03 14:00:00', 3);

ALTER TABLE `kategorie`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `uslugi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kategoria_id` (`kategoria_id`);

ALTER TABLE `kategorie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `uslugi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `uslugi`
  ADD CONSTRAINT `uslugi_ibfk_1` FOREIGN KEY (`kategoria_id`) REFERENCES `kategorie` (`id`);
COMMIT;

