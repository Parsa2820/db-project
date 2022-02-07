DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS EmployeeSchedule CASCADE;
DROP TABLE IF EXISTS RealPerson CASCADE;
DROP TABLE IF EXISTS Account CASCADE;
DROP TABLE IF EXISTS BankAccount CASCADE;
DROP TABLE IF EXISTS QarzolHasana CASCADE;
DROP TABLE IF EXISTS Saving CASCADE;
DROP TABLE IF EXISTS _Card CASCADE;
DROP TABLE IF EXISTS support CASCADE;
DROP TYPE IF EXISTS weekdayenum CASCADE;
DROP TABLE IF EXISTS _transaction CASCADE;
DROP TABLE IF EXISTS purchase CASCADE;
DROP TABLE IF EXISTS paybill CASCADE;
DROP TABLE IF EXISTS wiretransfer CASCADE;
DROP TABLE IF EXISTS deposit CASCADE;
DROP TABLE IF EXISTS withdraw CASCADE;
DROP TABLE IF EXISTS userrequest CASCADE;
DROP TABLE IF EXISTS createbankaccountrequest CASCADE;
DROP TABLE IF EXISTS createcardrequest CASCADE;
DROP TYPE IF EXISTS accounttype CASCADE;
DROP TYPE IF EXISTS weekdayenum CASCADE;
DROP TYPE IF EXISTS userrequeststatus CASCADE;



CREATE TABLE Employee (
    nationalId char(10),
    firstName varchar(30),
    lastName varchar(30),
    fatherName varchar(30),
    birthDate date,
    mobileNumber char(10),
    landlineNumber varchar(10),
    _role text,
    monthlySalary money,
    startDate date,
    postalCode char(10),
    country varchar(50),
    city varchar(50),
    addresExtra text,
    PRIMARY KEY(nationalId)
);

-- weekday enum
CREATE TYPE weekdayenum AS ENUM (
    'Saturday',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
);

CREATE TABLE EmployeeSchedule (
    emplyeeNationalId char(10),
    _weekDay weekdayenum,
    startHour time,
    endHour time,
    PRIMARY KEY(emplyeeNationalId, _weekDay),
    FOREIGN KEY(emplyeeNationalId) REFERENCES Employee(nationalId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE RealPerson (
    nationalId char(10),
    firstName varchar(30),
    lastName varchar(30),
    fatherName varchar(30),
    birthDate date,
    mobileNumber char(10),
    landlineNumber varchar(10),
    postalCode char(10),
    country varchar(50),
    city varchar(50),
    addresExtra text,
    PRIMARY KEY(nationalId)
);

CREATE TABLE Account (
    realPersonNationalId char(10),
    username varchar(30),
    email varchar(50),
    accountPassword char(32),
    phoneNumber char(10),
    PRIMARY KEY(username),
    FOREIGN KEY(realPersonNationalId) REFERENCES RealPerson(nationalId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE BankAccount (
    id int,
    active boolean,
    balance money,
    iban char(24),
    openDate date,
    creatorUsername varchar(30),
    PRIMARY KEY(id),
    FOREIGN KEY(creatorUsername) REFERENCES Account(username)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE QarzolHasana (
    id int,
    PRIMARY KEY(id),
    FOREIGN KEY(id) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Saving (
    id int,
    profit real,
    CHECK(
        0 < profit
        AND profit < 1
    ),
    PRIMARY KEY(id),
    FOREIGN KEY(id) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE _Card (
    cardNumber varchar(19),
    primaryPassword char(32),
    secondaryPassword char(32),
    expirationDate date,
    CVV1 varchar(4),
    CVV2 varchar(4),
    active boolean,
    bankAccount int,
    PRIMARY KEY(cardNumber),
    FOREIGN KEY(bankAccount) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE _Transaction (
    transactionId bigint,
    source int,
    destination int,
    _date date,
    _description text,
    amount money,
    trackingId bigint,
    PRIMARY KEY(transactionId),
    FOREIGN KEY(source) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(destination) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Purchase (
    transactionId bigint,
    storeName varchar(100),
    PRIMARY KEY(transactionId),
    FOREIGN KEY(transactionId) REFERENCES _Transaction(transactionId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE PayBill (
    transactionId bigint,
    billId varchar(13),
    paymentId varchar(13),
    PRIMARY KEY(transactionId),
    FOREIGN KEY(transactionId) REFERENCES _Transaction(transactionId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE WireTransfer (
    transactionId bigint,
    PRIMARY KEY(transactionId),
    FOREIGN KEY(transactionId) REFERENCES _Transaction(transactionId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Deposit (
    transactionId bigint,
    PRIMARY KEY(transactionId),
    FOREIGN KEY(transactionId) REFERENCES _Transaction(transactionId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Withdraw (
    transactionId bigint,
    PRIMARY KEY(transactionId),
    FOREIGN KEY(transactionId) REFERENCES _Transaction(transactionId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- user request status enum
CREATE TYPE userrequeststatus AS ENUM ('Pending', 'Done', 'Rejected');

CREATE TABLE UserRequest (
    requestId bigint,
    _status userrequeststatus,
    _date date,
    response text,
    _description text,
    PRIMARY KEY(requestId)
);

-- bank account type request enum
CREATE TYPE accounttype AS ENUM ('QarzolHasana', 'Saving');

CREATE TABLE CreateBankAccountRequest (
    requestId bigint,
    username varchar(30),
    bankAccountType accounttype,
    PRIMARY KEY(requestId),
    FOREIGN KEY(requestId) REFERENCES UserRequest(requestId)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(username) REFERENCES Account(username)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE CreateCardRequest (
    requestId bigint,
    bankAccountId int,
    PRIMARY KEY(requestId),
    FOREIGN KEY(requestId) REFERENCES UserRequest(requestId)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(bankAccountId) REFERENCES BankAccount(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE Support (
    requestId bigint,
    username varchar(30),
    employeeNationId char(10),
    PRIMARY KEY(requestId),
    FOREIGN KEY(requestId) REFERENCES UserRequest(requestId)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(username) REFERENCES Account(username)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(employeeNationId) REFERENCES Employee(nationalId)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);