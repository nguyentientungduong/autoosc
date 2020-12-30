Name:		autoosc
Version:  0.0.1
Release:  0
Summary:  Sample C program for OBS
Group:    Metapackages
License:  GPL-3.0
URL:      https://github.com/nguyentientungduong/autoosc

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	bash
BuildRequires:	cmake
Requires:	glibc
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
This is a sample of C project for publishing into OBS

%install
ls
cd helloworld
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc helloworld/LICENSE
%{_bindir}/*


%changelog

