pipeline {
    agent { 
        dockerfile { label 'ubuntu-slave-115'
                     dir 'doc'
                     filename 'dockerpythonfile' }
          }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
