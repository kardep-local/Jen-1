pipeline {
    agent { 
        dockerfile { label 'ubuntu-slave-115' }
          }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}
