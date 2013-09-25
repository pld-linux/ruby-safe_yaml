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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse YAML safely, without that pesky arbitrary object deserialization
vulnerability

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/safe_yaml.rb
%{ruby_vendorlibdir}/safe_yaml
