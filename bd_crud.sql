-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.3.16-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para bd_crud
CREATE DATABASE IF NOT EXISTS `bd_crud` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_danish_ci */;
USE `bd_crud`;

-- Volcando estructura para tabla bd_crud.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `G_id` int(11) NOT NULL AUTO_INCREMENT,
  `G_descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`G_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla bd_crud.grupo: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`G_id`, `G_descripcion`) VALUES
	(1, 'Activo'),
	(2, 'Pasivo'),
	(3, 'Patrimonio'),
	(5, 'Produccion'),
	(6, 'Ingreso');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla bd_crud.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Codigo` varchar(50) DEFAULT NULL,
  `Grupo` int(11) DEFAULT NULL,
  `Descripcion` varchar(50) DEFAULT NULL,
  `Naturaleza` varchar(50) DEFAULT NULL,
  `Estado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK__grupo` (`Grupo`),
  CONSTRAINT `FK__grupo` FOREIGN KEY (`Grupo`) REFERENCES `grupo` (`G_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla bd_crud.plancuenta: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
INSERT INTO `plancuenta` (`Id`, `Codigo`, `Grupo`, `Descripcion`, `Naturaleza`, `Estado`) VALUES
	(1, '01', 1, 'caja', 'D', b'1'),
	(2, '02', 1, 'banco', 'D', b'1'),
	(3, '03', 2, 'cuentax pagar', 'A', b'1'),
	(4, '04', 3, 'capital contable', 'A', b'1'),
	(5, '05', 5, 'ventas', 'A', b'1'),
	(6, '06', 6, 'compras', 'D', b'1'),
	(7, '07', 6, 'arriendo', 'D', b'0');
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
