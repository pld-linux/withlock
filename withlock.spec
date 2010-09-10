Summary:	A locking wrapper script
Name:		withlock
Version:	0.2
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	http://%{name}.googlecode.com/svn/trunk/withlock
# Source0-md5:	e3854a5c3e97121cd6a7e498ca77fbd5
URL:		http://code.google.com/p/withlock/
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
withlock is a locking wrapper script to make sure that some program
isn't run more than once. It is ideal to prevent periodic jobs spawned
by cron from stacking up.

The locks created are valid only while the wrapper is running, and
thus will never require additional cleanup, even after a reboot. This
makes the wrapper safe and easy to use, and much better than
implementing half-hearted locking within scripts.

%prep
%setup -qcT
%{__sed} -e '1s,^#!.*python,#!%{__python},' %{SOURCE0} >  %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/withlock
