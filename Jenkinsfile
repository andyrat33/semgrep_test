pipeline {
  agent any
  stages {
    stage('Build') {
        steps {
            sh 'echo "Building..."'
        }
    }

    stage('Test') {
        environment {
            SEMGREP_COMMIT = ${GIT_COMMIT}
        }
        steps {
            sh '''echo "Semgrep Testing..."
            echo "COMMIT ID ${GIT_COMMIT}"
            ls -la
            printenv
            docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 python -m semgrep_agent --config s/andyrat33:unsafe-crypto

            '''
        }
       }
  }

}