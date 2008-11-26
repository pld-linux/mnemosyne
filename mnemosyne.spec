Summary:	SuperMemo(tm)-like program 
Summary(pl.UTF-8):	Program podobny do SuperMemo
Name:		mnemosyne
Version:	1.1.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/mnemosyne-proj/%{name}-%{version}-r1.tgz
# Source0-md5:	2c08f6b0465f3280fcd2b17960b797bc
URL:		http://www.mnemosyne-proj.org/
BuildRequires:	python-PyQt
BuildRequires:	python-pygame
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-PyQt
Requires:	python-pygame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A flash card program to make your review process more efficient.

%description -l pl.UTF-8
Program podobny w działaniu do SuperMemo(tm).

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
%{_desktopdir}/*.desktop
%{_iconsdir}/*
