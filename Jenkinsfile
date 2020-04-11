pipeline {
    agent { docker { image 'maven:3.3.3'
                     label 'ubuntu-slave-115' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}
