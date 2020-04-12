pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker { image 'maven:3-alpine' 
                         label 'ubuntu-slave-115' } } 
            steps {
                sh 'mvn --version'
            }
        }
        stage('Front-end') {
            agent {
                docker { image 'node:7-alpine' 
                         label 'ubuntu-slave-115' } }
            steps {
                sh 'node --version'
            }
        }
    }
}
