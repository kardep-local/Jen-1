pipeline {
     agent {
	     docker { image 'maven:3-alpine'
		            label 'ubuntu-slave-115'
                args '-v $HOME/.m2:/root/.m2' }
		   }
     stages {
	    stage('Front-end') {
		    steps {
			     sh 'mvn -e -B'
				}
	                      }
	   } 
	 }
