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
            SEMGREP_COMMIT = "${env.GIT_COMMIT}"
            SEMGREP_REPO_NAME = env.GIT_URL.replaceFirst(/^https:\/\/github.com\/(.*).git$/, '$1')
            SEMGREP_REPO_URL = env.GIT_URL.replaceFirst(/^(.*).git$/,'$1')
            SEMGREP_JOB_URL = "${BUILD_URL}"
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
            SEMGREP_BRANCH = "${GIT_BRANCH}"
            BASELINE_REF = "${env.GIT_PREVIOUS_COMMIT}"
        }
        steps {
            sh '''echo "Semgrep Testing..."
            docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 \
            python -m semgrep_agent --config "p/r2c-ci" \
            --publish-deployment 63 \
            --publish-token $SEMGREP_APP_TOKEN


            '''
        }
       }

}
}