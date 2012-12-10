Summary:	Tibetan Machine Unicode font
Name:		fonts-ttf-tibetan-ttmuni
Version:	1.901b
Release:	%mkrel 5
License:	GPLv2+
URL: 		http://www.thdl.org/tools/fonts/tibfonts.php
Group:		System/Fonts/True type
Source0:	TibetanMachineUnicodeFont.zip
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mkfontdir

%description
This package provides an OpenType Unicode Tibetan font,
for writing in Tibetan, Dzongkha and Ladakhi with almost 4000 glyphs.

%prep
%setup -q -c %{name}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
install -m 644 *.ttf ${RPM_BUILD_ROOT}%{_datadir}/fonts/ttf/ttmuni/
cd ${RPM_BUILD_ROOT}/%{_datadir}/fonts/ttf/ttmuni/
mkfontdir
cp fonts.dir fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/ttmuni \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-tibetan-ttmuni:pri=50


%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(0644,root,root,0755)
%doc *.txt
%{_datadir}/fonts/ttf/ttmuni/
%{_sysconfdir}/X11/fontpath.d/ttf-tibetan-ttmuni:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.901b-5mdv2011.0
+ Revision: 675577
+ rebuild (emptylog)

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 1.901b-4mdv2011.0
+ Revision: 611717
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.901b-3mdv2010.1
+ Revision: 494157
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.901b-2mdv2010.0
+ Revision: 428852
- rebuild

* Sat Sep 27 2008 Frederic Crozat <fcrozat@mandriva.com> 1.901b-1mdv2009.0
+ Revision: 288921
- Release 1.901b
- Remove obsolete fontconfig 1 cache file
- Fix url

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.1.1-0.alpha.2mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1.1-0.alpha.2mdv2008.0
+ Revision: 49209
- fontpath.d conversion (#31756)
- Import fonts-ttf-tibetan-ttmuni



* Wed Aug 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.1.1.1-0.alpha.1mdv2007.0
- First Mandriva release (Davide Duina <davide.duina[at]google.com>)
- fix URL
- use %%mkrel
