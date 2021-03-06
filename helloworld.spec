Name:		helloworld
Version:	1.0.0
Release:	1%{?dist}
Summary:	Sample C program for OBS

Group:		Documentation
License:	GPL-3.0
URL:		https://github.com/oanhltko/chello
Source0:	helloworld-1.0.0.tar.gz

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
cd helloworld
make %{?_smp_mflags}


%install
cd helloworld
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc helloworld/LICENSE
%{_bindir}/*


%changelog

