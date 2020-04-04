pipeline {
    agent {
  label 'ubuntu-slave-111'
}
    stages {
        stage('build') {
            steps {
                echo '"Running shell script"'
                sh label: '', script: '/tmp/pankaj.sh'
                echo '"Running free style jenkins job"'
                build 'Test-Job'
                echo '"Waiting for 10 seconds"'
                sleep 10
                echo '"Deleting workspace directory"'
                cleanWs()
            }
        }
    }
}
