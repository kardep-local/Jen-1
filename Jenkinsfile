pipeline {
    agent { 
        dockerfile { label 'ubuntu-slave-115'
                     dir 'doc'
                     filename 'dockerpythonfile'
                     args '-t python-test-app .' }
          }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
