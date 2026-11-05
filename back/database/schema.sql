-- Reference MySQL 8 schema. The Flask CLI creates the same schema from SQLAlchemy models.
CREATE DATABASE IF NOT EXISTS AssetVerifyApp
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE AssetVerifyApp;

CREATE TABLE IF NOT EXISTS user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(80) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(40) NOT NULL DEFAULT 'staff',
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS asset_sequence (
  id INT PRIMARY KEY,
  next_value INT NOT NULL
);

CREATE TABLE IF NOT EXISTS asset (
  id INT AUTO_INCREMENT PRIMARY KEY,
  asset_id VARCHAR(24) NOT NULL UNIQUE,
  name VARCHAR(140) NOT NULL,
  category VARCHAR(80) NOT NULL,
  serial_number VARCHAR(100) NOT NULL UNIQUE,
  department VARCHAR(100) NOT NULL,
  location VARCHAR(140) NOT NULL,
  assigned_to VARCHAR(120) NOT NULL,
  purchase_date DATE NOT NULL,
  status VARCHAR(40) NOT NULL DEFAULT 'Active',
  description TEXT,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX ix_asset_status (status), INDEX ix_asset_created_at (created_at)
);

CREATE TABLE IF NOT EXISTS verification (
  id INT AUTO_INCREMENT PRIMARY KEY,
  asset_id INT NOT NULL,
  result VARCHAR(40) NOT NULL,
  remarks VARCHAR(500),
  verified_by VARCHAR(80) NOT NULL,
  verified_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX ix_verification_result (result), INDEX ix_verification_verified_at (verified_at),
  CONSTRAINT fk_verification_asset FOREIGN KEY (asset_id) REFERENCES asset(id) ON DELETE CASCADE
);
