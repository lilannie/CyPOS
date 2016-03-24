INSERT INTO db309grp17.base_courses (acronym, name, description, numCredits)
SELECT number, name, description, numCredits
FROM db309grp17.courses_courses

ALTER TABLE db309grp17.courses_courses CHANGE COLUMN `number` `number` longtext NOT NULL DEFAULT '' ;