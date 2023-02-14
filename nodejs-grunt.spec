%global enable_tests 0

Name:       nodejs-grunt
Version:    1.6.1
Release:    1
Summary:    Grunt is a JavaScript library used for automation and running tasks
License:    MIT
URL:        https://github.com/gruntjs/grunt
Source0:    https://github.com/gruntjs/grunt/archive/v%{version}/grunt-%{version}.tar.gz
Group:      Development/Other

BuildArch:  noarch
BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(dateformat)
BuildRequires:  npm(eventemitter2)
BuildRequires:  npm(exit)
BuildRequires:  npm(findup-sync)
BuildRequires:  npm(glob)
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-known-options)
BuildRequires:  npm(grunt-legacy-log)
BuildRequires:  npm(grunt-legacy-util)
BuildRequires:  npm(iconv-lite)
BuildRequires:  npm(js-yaml)
BuildRequires:  npm(minimatch)
BuildRequires:  npm(nopt)
BuildRequires:  npm(path-is-absolute)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(difflet)
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(grunt-contrib-watch)
BuildRequires:  npm(semver)
BuildRequires:  npm(shelljs)
BuildRequires:  npm(temporary)
BuildRequires:  npm(through2)
%endif


%description
Grunt is the JavaScript task runner. Why use a task runner? In one word:
automation. The less work you have to do when performing repetitive tasks
like minification, compilation, unit testing, linting, etc, the easier
your job becomes. After you've configured it, a task runner can do most
of that mundane work for you with basically zero effort.

%prep
%setup -n grunt-%{version}

%nodejs_fixdep coffee-script '~1.3'
%nodejs_fixdep dateformat '*'
%nodejs_fixdep eventemitter2 '~0.4'
%nodejs_fixdep findup-sync '~0.1'
%nodejs_fixdep glob '~6.0.3'
%nodejs_fixdep minimatch '~3.0.0'
%nodejs_fixdep nopt '^3.0.6'
%nodejs_fixdep rimraf '~2.0'
%nodejs_fixdep js-yaml '^3.5.0'



%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt
cp -pr package.json internal-tasks/ lib/ \
    %{buildroot}%{nodejs_sitelib}/grunt

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
grunt nodeunit:all
%endif


%files
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%{nodejs_sitelib}/grunt
