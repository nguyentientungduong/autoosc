Name:		helloworld
Version:	0.0.1
Release:	1%{?dist}
Summary:	Sample C program for OBS

Group:		Documentation
License:	GPL-3.0
URL:		https://github.com/oanhltko/chello
Source0:	autoosc-0.0.1.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	bash
BuildRequires:	cmake
Requires:	glibc
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
This is a sample of C project for publishing into OBS

%prep
%setup -q -n %{name}-%{version}


%build
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/*


%changelog

