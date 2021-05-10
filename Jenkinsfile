pipeline {
  agent {
    docker {
      image 'returntocorp/semgrep-agent:v1'
      args '-u root'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building..."'
      }
    }

    stage('Semgrep_agent') {
      parallel {
        stage('Semgrep_agent') {
          environment {
            SEMGREP_COMMIT = "${env.GIT_COMMIT}"
            SEMGREP_REPO_NAME = env.GIT_URL.replaceFirst(/^https:\/\/github.com\/(.*).git$/, '$1')
            SEMGREP_REPO_URL = env.GIT_URL.replaceFirst(/^(.*).git$/,'$1')
            SEMGREP_JOB_URL = "${BUILD_URL}"
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
            SEMGREP_DEPLOYMENT_ID = credentials('SEMGREP_DEPLOYMENT_ID')
            SEMGREP_BRANCH = "${GIT_BRANCH}"
          }
          steps {
            sh 'python -m semgrep_agent --config "p/r2c-ci" --publish-token $SEMGREP_APP_TOKEN --publish-deployment $SEMGREP_DEPLOYMENT_ID'
          }
        }

        stage('Dependency-Check') {
          steps {
            sh '''/var/lib/jenkins/tools/org.jenkinsci.plugins.DependencyCheck.tools.DependencyCheckInstallation/dependency-check/dependency-check/bin/dependency-check.sh --scan $WORKSPACE 
            echo $(pwd)
'''
          }
        }

      }
    }

  }
}