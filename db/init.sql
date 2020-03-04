CREATE DATABASE figaro;
use figaro;

CREATE TABLE Barbershops (
  id      VARCHAR(10)   PRIMARY KEY NOT NULL,
  name    VARCHAR(50)   NOT NULL,
  address VARCHAR(200)  NOT NULL,
  rating  FLOAT,
  coordX  FLOAT,
  coordY  FLOAT
);

CREATE TABLE Barbers (
  id      VARCHAR(10)   PRIMARY KEY NOT NULL,
  name    VARCHAR(50)   NOT NULL,
  rating  FLOAT,
  bbs_id    VARCHAR(50)   NOT NULL,
  FOREIGN KEY(bbs_id) REFERENCES Barbershops(id)
);

CREATE TABLE Clients (
  id        VARCHAR(50)   PRIMARY KEY NOT NULL,
  name      VARCHAR(50)   NOT NULL,
  phone     VARCHAR(10),
  sex       CHAR(1),
  birthday  DATE,
  rating    FLOAT
);

CREATE TABLE Services (
  id VARCHAR(10)      NOT NULL PRIMARY KEY,
  name VARCHAR(50)    NOT NULL,
  price INTEGER,
  bbs_id  VARCHAR(50) NOT NULL,
  FOREIGN KEY(bbs_id) REFERENCES Barbershops(id)
);

CREATE TABLE Appointments (
  id VARCHAR(10)          NOT NULL PRIMARY KEY,
  date VARCHAR(12)        NOT NULL,
  time VARCHAR(6),
  barber_id VARCHAR(50)   NOT NULL,
  client_id VARCHAR(50)   NOT NULL,
  service_id VARCHAR(50)  NOT NULL,
  FOREIGN KEY(barber_id) REFERENCES Barbers(id),
  FOREIGN KEY(client_id) REFERENCES Clients(id),
  FOREIGN KEY(service_id) REFERENCES Services(id)
);

INSERT INTO Barbershops
  (id, name, address, coordX, coordY)
VALUES
  ('bbs_000001', 'Vagabond Hair Studio', 'Bloc G1, Bulevardul Unirii 65, Bucuresti', 44.426309, 26.123891),
  ('bbs_000002', 'Office 21 Barbershop', 'Strada Inginer Cristian Pascal 34, Bucuresti', 44.450964, 26.054762);

INSERT INTO Barbers
  (id, name, bbs_id)
VALUES
  ('b_00000001', 'Ionutz', 'bbs_000001'),
  ('b_00000002', 'Mihai', 'bbs_000002');

INSERT INTO Clients
  (id, name, phone, sex)
VALUES
  ('victor.andreescu@gmail.com', 'Victor', '0762789134', 'M'),
  ('andrew.young@yahoo.co.uk', 'Andrei', '0743671629', 'M');

INSERT INTO Services
  (id, name, price, bbs_id)
VALUES
  ('s_00000001', 'Tuns modern', 50, 'bbs_000001'),
  ('s_00000002', 'Tuns cu ciobul', 5, 'bbs_000002');

INSERT INTO Appointments
  (id, date, time, barber_id, client_id, service_id)
VALUES
  ('a_00000001', '29-Mar-2020', '10:00', 'b_00000001', 'victor.andreescu@gmail.com', 's_00000001'),
  ('a_00000002', '29-Mar-2020', '16:30', 'b_00000002', 'andrew.young@yahoo.co.uk', 's_00000002');