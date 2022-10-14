CREATE DATABASE IF NOT EXISTS hospitaldb;
USE hospitaldb;


#ENTITYS 


CREATE TABLE if not exists users(
			id VARCHAR(100),
       	    username VARCHAR(100) not null,
       	    password VARCHAR(100) not null,
       	    job VARCHAR(100) not null,
       	    PRIMARY KEY (id)
       );
       
CREATE TABLE if not exists department(
			id VARCHAR(100), 
            name VARCHAR(100) not null,
            PRIMARY KEY (id)
            
	   );
CREATE TABLE if not exists doctors(
			id VARCHAR(100),
       	    name VARCHAR(100) not null,
       	    sex VARCHAR(100) not null,
            d_id VARCHAR(100) not null,
       	    PRIMARY KEY (id),
            FOREIGN KEY (id) REFERENCES users(id),
            FOREIGN KEY (d_id) REFERENCES department(id)
       );
CREATE TABLE if not exists nurses(
			id VARCHAR(100),
       	    name VARCHAR(100) not null,
       	    sex VARCHAR(100) not null,
            d_id VARCHAR(100) not null,
       	    PRIMARY KEY (id),
            FOREIGN KEY (id) REFERENCES users(id),
            FOREIGN KEY (d_id) REFERENCES department(id)
       );
       
CREATE TABLE if not exists patients(
			id VARCHAR(100),
       	    name VARCHAR(100) not null,
       	    nationalid VARCHAR(100) not null,
            sex VARCHAR(100) not null,
            dob VARCHAR(100) not null,
            balance DECIMAL(10,2) not null,
            photo VARCHAR(100) not null,
            n_id VARCHAR(100),
       	    PRIMARY KEY (id),
            FOREIGN KEY (id) REFERENCES nurses(id),
            FOREIGN KEY (id) REFERENCES users(id)
       );

CREATE TABLE if not exists checklist(
			id VARCHAR(100), 
            time VARCHAR(100) not null,
            PRIMARY KEY (id)
	   );
CREATE TABLE if not exists checkitem(
			id VARCHAR(100), 
            name VARCHAR(100) not null,
            price decimal(10,2) not null,
            intro VARCHAR(100) not null,
            PRIMARY KEY (id)
	   );
CREATE TABLE if not exists prescription(
			id VARCHAR(100), 
            time VARCHAR(100) not null,
            PRIMARY KEY (id)
	   );
CREATE TABLE if not exists medicine(
			id VARCHAR(100), 
            name VARCHAR(100) not null,
            price decimal(10,2) not null,
            intro VARCHAR(100) not null,
            PRIMARY KEY (id)
	   );
CREATE TABLE if not exists account(
			id VARCHAR(100), 
            type VARCHAR(100) not null,
            balance decimal(10,2) not null,
            reason VARCHAR(100) not null,
            time VARCHAR(100) not null,
            p_id VARCHAR(100) not null,
            PRIMARY KEY (id),
            FOREIGN KEY (p_id) REFERENCES patients(id)
	   );
       
CREATE TABLE if not exists room(
			id VARCHAR(100), 
            vacancy INTEGER not null,
            price DECIMAL(10,2) not null,
            d_id VARCHAR(100),
            n_id VARCHAR(100),
            PRIMARY KEY (id),
            FOREIGN KEY (d_id) REFERENCES department(id),
            FOREIGN KEY (n_id) REFERENCES nurses(id)
		
	   );
       
CREATE TABLE if not exists bed(
			id VARCHAR(100), 
            patient VARCHAR(100),
            time VARCHAR(100) not null,
            r_id VARCHAR(100) not null,
            PRIMARY KEY (id),
            FOREIGN KEY (r_id) REFERENCES room(id)
	   );

       
#RELATIONS


CREATE TABLE if not exists doctor_patient(
			d_id VARCHAR(100), 
            p_id VARCHAR(100),
            FOREIGN KEY (d_id) REFERENCES doctors(id),
            FOREIGN KEY (p_id) REFERENCES patients(id)
            
	   );
CREATE TABLE if not exists r_checklist(
			d_id VARCHAR(100), 
            p_id VARCHAR(100),
            cl_id VARCHAR(100), 
            ci_id VARCHAR(100),
            FOREIGN KEY (d_id) REFERENCES doctors(id),
            FOREIGN KEY (p_id) REFERENCES patients(id),
            FOREIGN KEY (cl_id) REFERENCES checklist(id),
            FOREIGN KEY (ci_id) REFERENCES checkitem(id)
            
	   );
CREATE TABLE if not exists r_prescription(
			d_id VARCHAR(100), 
            p_id VARCHAR(100),
            pr_id VARCHAR(100), 
		    m_id VARCHAR(100),
            FOREIGN KEY (d_id) REFERENCES doctors(id),
            FOREIGN KEY (p_id) REFERENCES patients(id),
            FOREIGN KEY (pr_id) REFERENCES prescription(id),
            FOREIGN KEY (m_id) REFERENCES medicine(id)
            
	   );
       
CREATE TABLE if not exists patient_bed(
			p_id VARCHAR(100), 
            b_id VARCHAR(100),
            FOREIGN KEY (p_id) REFERENCES patients(id),
            FOREIGN KEY (b_id) REFERENCES bed(id)
            
	   );

       






	
       
       