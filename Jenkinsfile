pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            agent { label 'ubuntu-slave-115' }
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}
