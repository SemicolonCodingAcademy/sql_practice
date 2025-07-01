-- 사용자 정보
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    gpa FLOAT,
    test_scores JSON,
    extracurricular JSON,
    created_at TIMESTAMP
);

-- 대학 정보
CREATE TABLE universities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200),
    admission_requirements JSON,
    acceptance_rate FLOAT,
    average_gpa FLOAT,
    average_scores JSON
);

-- 분석 결과
CREATE TABLE analysis_results (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    university_id INT,
    admission_probability FLOAT,
    improvement_suggestions TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (university_id) REFERENCES universities(id)
);
