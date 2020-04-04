pipeline {
    agent {
  label 'ubuntu-slave-111'
}
    stages {
        stage('build') {
            steps {
                sh label: '', script: '/tmp/pankaj.sh'
            }
        }
    }
}
