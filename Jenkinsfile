pipeline {
    agent { 
        dockerfile { label 'ubuntu-slave-115'
                     dir 'doc'
                     filename 'newdockerfile'
                     args '-v /tmp:/tmp' }
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
