DROP TRIGGER account_password_hash_trigger ON Account;
DROP TRIGGER card_passwords_hash_trigger ON _Card;
DROP TRIGGER transaction_trigger ON _Transaction;
DROP TRIGGER BankAccountCreate ON UserRequest;


CREATE OR REPLACE FUNCTION hash_password()
  RETURNS trigger AS
$$
BEGIN
NEW.accountPassword := MD5(NEW.accountPassword);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER account_password_hash_trigger
  BEFORE INSERT
  ON Account
  FOR EACH ROW
  EXECUTE PROCEDURE hash_password();


CREATE OR REPLACE FUNCTION hash_passwords()
  RETURNS trigger AS
$$
BEGIN
NEW.primaryPassword := MD5(NEW.primaryPassword);
NEW.secondaryPassword := MD5(NEW.secondaryPassword);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER card_passwords_hash_trigger
  BEFORE INSERT
  ON _Card
  FOR EACH ROW
  EXECUTE PROCEDURE hash_passwords();


CREATE OR REPLACE FUNCTION apply_transaction()
  RETURNS trigger AS
$$
BEGIN
    IF (SELECT balance FROM BankAccount WHERE BankAccount.id = NEW.source) < NEW.amount THEN
        RAISE EXCEPTION 'Insufficient balance'; 
    ELSE
        UPDATE BankAccount SET balance = balance - NEW.amount WHERE BankAccount.id = NEW.source;
        UPDATE BankAccount SET balance = balance + NEW.amount WHERE BankAccount.id = NEW.destination;
    END IF; 
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER transaction_trigger
  BEFORE INSERT
  ON _Transaction
  FOR EACH ROW
  EXECUTE PROCEDURE apply_transaction();


CREATE OR REPLACE FUNCTION bank_account() 
   RETURNS TRIGGER 
    AS $$
    BEGIN
        IF NEW._status = 'Done' THEN
            IF (SELECT bankAccountType FROM CreateBankAccountRequest WHERE CreateBankAccountRequest.requestId = NEW.requestId) = 'Saving' THEN
                INSERT INTO BankAccount VALUES((SELECT max(id)+1 FROM BankAccount), True, 0, NULL, CURRENT_TIMESTAMP::date, (SELECT username FROM CreateBankAccountRequest WHERE CreateBankAccountRequest.requestId = NEW.requestId));
                INSERT INTO Saving VALUES((SELECT max(id) FROM BankAccount), 0.1);
            ELSE
                INSERT INTO BankAccount VALUES((SELECT max(id)+1 FROM BankAccount), True, 0, NULL, CURRENT_TIMESTAMP::date, (SELECT username FROM CreateBankAccountRequest WHERE CreateBankAccountRequest.requestId = NEW.requestId));
                INSERT INTO QarzolHasana VALUES((SELECT max(id) FROM BankAccount));
            END IF;
        END IF;
        RETURN NEW;
    END;
    $$
LANGUAGE PLPGSQL;
CREATE TRIGGER BankAccountCreate AFTER UPDATE ON UserRequest
    FOR EACH ROW
    EXECUTE PROCEDURE bank_account();