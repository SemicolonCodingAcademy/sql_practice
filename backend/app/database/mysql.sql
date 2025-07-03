-- 데이터베이스 생성
CREATE DATABASE student_management;
USE student_management;

-- 학생 정보 테이블
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    grade INT,
    school VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 학업 성적 테이블
CREATE TABLE academic_records (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    semester VARCHAR(20),
    subject VARCHAR(50),
    score FLOAT,
    grade VARCHAR(2),
    credit INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 활동 기록 테이블
CREATE TABLE activities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    activity_type ENUM('교내활동', '교외활동', '수상실적', '봉사활동', '자격증', '어학성적'),
    title VARCHAR(200),
    description TEXT,
    start_date DATE,
    end_date DATE,
    achievement TEXT,
    proof_document VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 대학 정보 테이블
CREATE TABLE universities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(100),
    admission_type VARCHAR(50),
    required_subjects TEXT,
    min_gpa FLOAT,
    additional_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 대학 지원 계획 테이블
CREATE TABLE university_applications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    university_id INT,
    priority INT,
    status ENUM('관심', '지원예정', '지원완료', '합격', '불합격'),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (university_id) REFERENCES universities(id)
);

-- AI 분석 결과 테이블
CREATE TABLE analysis_results (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    analysis_type ENUM('성적분석', '활동분석', '대학적합도', '개선제안'),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
