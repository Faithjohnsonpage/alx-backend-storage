-- This SQL script creates a stored procedure ComputeAverageScoreForUser that
-- computes and stores the average score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_value FLOAT;

    SELECT AVG(score) INTO average_value
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users SET average_score = average_value
    WHERE id = user_id;
END$$

DELIMITER ;
