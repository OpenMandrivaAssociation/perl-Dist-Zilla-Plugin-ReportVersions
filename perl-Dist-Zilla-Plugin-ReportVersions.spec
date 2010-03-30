%define upstream_name    Dist-Zilla-Plugin-ReportVersions
%define upstream_version 1.100880

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Write a test that reports used module versions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Moose)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files

  t/000-report-versions.t

The '000' prefix is chosen so it runs first to make sure it shows up in
CPAN tester reports.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%perl_vendorlib/*


