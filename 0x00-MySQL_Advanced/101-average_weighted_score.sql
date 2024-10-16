-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS u, 
    (SELECT u.id, SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg 
    FROM users AS u 
    JOIN corrections AS c ON u.id = c.user_id 
    JOIN projects AS p ON c.project_id = p.id 
    GROUP BY u.id)
  AS w
  SET u.average_score = w.weighted_avg 
  WHERE u.id = w.id;
END;
