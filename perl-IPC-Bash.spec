#
# spec file for package perl-IPC-Bash (Version 0.0.2)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name IPC-Bash
Name:           perl-IPC-Bash
Version:        0.0.2
Release:        0
License:        Artistic-1.0 or GPL-1.0-or-later
Summary:        Library for interracting with bash session
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  (rpm-build-perl or perl-generators)
Requires:       (dash or bash or zsh or sh or tcsh or ksh)
%{perl_requires}

%description
Library for interracting with bash session

%prep
%autosetup  -n %{cpan_name}-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc README
%license LICENSE

%changelog
