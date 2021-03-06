DELETE FROM realperson;
DELETE FROM employee;
DELETE FROM employeeSchedule;
DELETE FROM account;
DELETE FROM bankAccount;
DELETE FROM qarzolHasana;
DELETE FROM saving;
DELETE FROM _card;
DELETE FROM _transaction;
DELETE FROM purchase;
DELETE FROM payBill;
DELETE FROM wireTransfer;
DELETE FROM deposit;
DELETE FROM withdraw;
DELETE FROM userRequest;
DELETE FROM createBankAccountRequest;
DELETE FROM createCardRequest;
DELETE FROM support;
DELETE FROM realperson;
DELETE FROM employee;
DELETE FROM employeeSchedule;
DELETE FROM account;
DELETE FROM bankAccount;
DELETE FROM qarzolHasana;
DELETE FROM saving;
DELETE FROM _card;
DELETE FROM _transaction;
DELETE FROM purchase;
DELETE FROM payBill;
DELETE FROM wireTransfer;
DELETE FROM deposit;
DELETE FROM withdraw;
DELETE FROM userRequest;
DELETE FROM createBankAccountRequest;
DELETE FROM createCardRequest;
DELETE FROM support;

insert into  RealPerson(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111112',
    'azra',
    'abi',
    'brim',
    '1/1/2001',
    '0911222335',
    '0216666666',
    '1231231231',
    'france',
    'paris',
    'main street'
);

insert into Employee(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    _role,
    monthlySalary,
    startDate,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111112',
    'azra',
    'abi',
    'brim',
    '1/1/2001',
    '0911222334',
    '0216666666',
    'Employee',
    '1111111',
    '1/1/2020',
    '1231231231',
    'france',
    'paris',
    'main street'
);

insert into EmployeeSchedule (
    emplyeeNationalId,
    _weekDay,
    startHour,
    endHour
)

VALUES(
    '1111111112',
    'Saturday',
    '8:00',
    '16:00'
);

insert into Account(
    realPersonNationalId,
    username,
    email,
    accountPassword,
    phoneNumber
)

VALUES(
    '1111111112',
    'azra',
    'azra@gmail.com',
    'f0e4c2f76c58916ec258f246851bea3b',
    '0912222222'
);

insert into BankAccount(
    id,
    active,
    balance,
    iban,
    openDate,
    creatorUsername
)

VALUES(
    121212,
    'True',
    '1111111',
    '1111111111111111111111',
    '1/2/2020',
    'azra'
);

insert into BankAccount(
    id,
    active,
    balance,
    iban,
    openDate,
    creatorUsername
)

VALUES(
    121213,
    'True',
    '1111111',
    '1111111111111121111111',
    '1/2/2020',
    'azra'
);

insert into QarzolHasana(
    id
)

VALUES(
    121212
);

insert into Saving(
    id,
    profit
)

VALUES(
    121213,
    0.1
);

insert into _Card(
    cardNumber,
    primaryPassword,
    secondaryPassword,
    expirationDate,
    CVV1,
    CVV2,
    active,
    bankAccount
)

VALUES(
    '111111111111111111',
    '1111',
    '11111111',
    '1/1/2222',
    '1111',
    '1111',
    'True',
    121212
);

insert into _Transaction(
    transactionId,
    source,
    destination,
    _date,
    _description,
    amount,
    trackingId
)

VALUES(
    '1212121',
    121212,
    121213,
    '1/3/2020',
    'store',
    '11111',
    '123123123'
);

insert into Purchase(
    transactionId,
    storeName
)

VALUES(
    1212121,
    'digikala'
);

insert into PayBill(
    transactionId,
    billId,
    paymentId
)

VALUES(
    1212121,
    '1111111111111',
    '111111111111'
);

insert into WireTransfer(
    transactionId
)

VALUES(
    1212121
);

insert into Deposit(
    transactionId
)

VALUES(
    1212121
);

insert into Withdraw(
    transactionId
)

VALUES(
    1212121
);

insert into UserRequest(
    requestId,
    _status,
    _date,
    response,
    _description
)

VALUES(
    121212,
    'Done',
    '1/2/2020',
    'yes',
    'ok'
);


insert into CreateBankAccountRequest(
    requestId,
    username,
    bankAccountType
)

VALUES(
    121212,
    'azra',
    'QarzolHasana'
);

insert into CreateCardRequest(
    requestId,
    bankAccountId
)

VALUES(
    121212,
    121212
);

insert into Support(
    requestId,
    username,
    employeeNationId
)

VALUES(
    121212,
    'azra',
    '1111111112'
);

insert into  RealPerson(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111444',
    'angela',
    'pitt',
    'brad',
    '1/2/2001',
    '0911222444',
    '0216666444',
    '1231231444',
    'france',
    'paris',
    'route street'
);

insert into Employee(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    _role,
    monthlySalary,
    startDate,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111444',
    'angela',
    'pitt',
    'brad',
    '1/2/2001',
    '0911222444',
    '0216666444',
    'Employee',
    '11111444',
    '1/2/2020',
    '1231231444',
    'france',
    'paris',
    'route street'
);

insert into EmployeeSchedule (
    emplyeeNationalId,
    _weekDay,
    startHour,
    endHour
)

VALUES(
    '1111111444',
    'Saturday',
    '8:00',
    '16:00'
);

insert into Account(
    realPersonNationalId,
    username,
    email,
    accountPassword,
    phoneNumber
)

VALUES(
    '1111111444',
    'angela',
    'angela@gmail.com',
    'f0e4c2f76c58916ec258f246851be444',
    '0912222444'
);

insert into BankAccount(
    id,
    active,
    balance,
    iban,
    openDate,
    creatorUsername
)

VALUES(
    121444,
    'True',
    '1111444',
    '1111111111111111111444',
    '1/4/2020',
    'angela'
);

insert into QarzolHasana(
    id
)

VALUES(
    121444
);

insert into _Card(
    cardNumber,
    primaryPassword,
    secondaryPassword,
    expirationDate,
    CVV1,
    CVV2,
    active,
    bankAccount
)

VALUES(
    '111111111111111444',
    '1444',
    '11111444',
    '1/1/2222',
    '1444',
    '1444',
    'True',
    121444
);

insert into _Transaction(
    transactionId,
    source,
    destination,
    _date,
    _description,
    amount,
    trackingId
)

VALUES(
    '1212444',
    121444,
    121212,
    '1/4/2020',
    'store',
    '11144',
    '123123444'
);

insert into Purchase(
    transactionId,
    storeName
)

VALUES(
    1212444,
    'digikala'
);

insert into PayBill(
    transactionId,
    billId,
    paymentId
)

VALUES(
    1212444,
    '1111111111444',
    '111111111444'
);

insert into WireTransfer(
    transactionId
)

VALUES(
    1212444
);

insert into Deposit(
    transactionId
)

VALUES(
    1212444
);

insert into Withdraw(
    transactionId
)

VALUES(
    1212444
);

insert into UserRequest(
    requestId,
    _status,
    _date,
    response,
    _description
)

VALUES(
    121444,
    'Done',
    '1/4/2020',
    'accepted',
    'ok'
);


insert into CreateBankAccountRequest(
    requestId,
    username,
    bankAccountType
)

VALUES(
    121444,
    'angela',
    'QarzolHasana'
);

insert into CreateCardRequest(
    requestId,
    bankAccountId
)

VALUES(
    121444,
    121444
);

insert into Support(
    requestId,
    username,
    employeeNationId
)

VALUES(
    121444,
    'angela',
    '1111111444'
);


insert into  RealPerson(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111155',
    'jacob',
    'obama',
    'barak',
    '1/1/1998',
    '0911222355',
    '0216666655',
    '1231231255',
    'france',
    'paris',
    '55 street'
);

insert into Employee(
    nationalId,
    firstName,
    lastName,
    fatherName,
    birthDate,
    mobileNumber,
    landlineNumber,
    _role,
    monthlySalary,
    startDate,
    postalCode,
    country,
    city,
    addresExtra
)

VALUES(
    '1111111155',
    'jacob',
    'barak',
    'obama',
    '1/1/1998',
    '0911222355',
    '0216666655',
    'Employee',
    '1111155',
    '1/5/2020',
    '1231231255',
    'france',
    'paris',
    '55 street'
);

insert into EmployeeSchedule (
    emplyeeNationalId,
    _weekDay,
    startHour,
    endHour
)

VALUES(
    '1111111155',
    'Saturday',
    '8:00',
    '16:00'
);

insert into Account(
    realPersonNationalId,
    username,
    email,
    accountPassword,
    phoneNumber
)

VALUES(
    '1111111155',
    'jacob',
    'jacob@gmail.com',
    'f0e4c2f76c58916ec258f246851bea55',
    '0912222255'
);

insert into BankAccount(
    id,
    active,
    balance,
    iban,
    openDate,
    creatorUsername
)

VALUES(
    1212155,
    'True',
    '1111155',
    '1111111111111111111155',
    '1/5/2020',
    'jacob'
);

insert into QarzolHasana(
    id
)

VALUES(
    1212155
);

insert into Saving(
    id,
    profit
)

VALUES(
    1212155,
    0.1
);

insert into _Card(
    cardNumber,
    primaryPassword,
    secondaryPassword,
    expirationDate,
    CVV1,
    CVV2,
    active,
    bankAccount
)

VALUES(
    '111111111111111155',
    '1155',
    '11111155',
    '1/5/2222',
    '1155',
    '1155',
    'True',
    121444
);

insert into _Transaction(
    transactionId,
    source,
    destination,
    _date,
    _description,
    amount,
    trackingId
)

VALUES(
    '1212155',
    121212,
    121444,
    '1/5/2020',
    'store',
    '11155',
    '123123155'
);

insert into Purchase(
    transactionId,
    storeName
)

VALUES(
    1212155,
    'digikala'
);
