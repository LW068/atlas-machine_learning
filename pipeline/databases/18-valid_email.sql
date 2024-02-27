-- Creates a trigger that resets the valid_email attribute when the email is changed
DELIMITER $$
CREATE TRIGGER BeforeEmailUpdate
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = FALSE;
  END IF;
END$$
DELIMITER ;
