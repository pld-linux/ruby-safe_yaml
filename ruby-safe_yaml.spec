#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	safe_yaml
Summary:	Parse YAML safely
Name:		ruby-%{pkgname}
Version:	0.9.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	9788eb941a0935853679ee186a3d481b
URL:		http://dtao.github.com/safe_yaml/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-hashie
BuildRequires:	ruby-heredoc_unindent
BuildRequires:	ruby-ostruct
BuildRequires:	ruby-rspec
BuildRequires:	ruby-yaml
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse YAML safely, without that pesky arbitrary object deserialization
vulnerability

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
rspec -Ilib spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGES.md LICENSE.txt
%{ruby_vendorlibdir}/safe_yaml.rb
%{ruby_vendorlibdir}/safe_yaml
%{ruby_specdir}/safe_yaml-%{version}.gemspec
