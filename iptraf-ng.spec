Summary:	IPTraf is a console-based network monitoring program
Summary(es.UTF-8):	Herramienta para verificación de redes desde consolas
Summary(pl.UTF-8):	IPTraf służy do monitorowania sieci
Summary(pt_BR.UTF-8):	Ferramenta baseada no console para monitoração de rede
Summary(ru.UTF-8):	IPTraf - консольная программа мониторинга сетевого траффика
Summary(uk.UTF-8):	IPTraf - консольна програма моніторингу трафіку в мережі
Name:		iptraf-ng
Version:	1.1.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	https://fedorahosted.org/releases/i/p/iptraf-ng/%{name}-%{version}.tar.gz
# Source0-md5:	de27cfeeede96e2acfb0edc8439b034a
Patch0:		%{name}-format-security.patch
Patch1:		0001-BUGFIX-fix-Floating-point-exception-in-tcplog_flowra.patch
URL:		https://fedorahosted.org/iptraf-ng/
BuildRequires:	ncurses-ext-devel >= 5.4
Obsoletes:	iptraf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPTraf is a console-based network monitoring utility. IPTraf gathers
data like TCP connection packet and byte counts, interface statistics
and activity indicators, TCP/UDP traffic breakdowns, and LAN station
packet and byte counts. IPTraf features include an IP traffic monitor
which shows TCP flag information, packet and byte counts, ICMP
details, OSPF packet types, and oversized IP packet warnings;
interface statistics showing IP, TCP, UDP, ICMP, non-IP and other IP
packet counts, IP checksum errors, interface activity and packet size
counts; a TCP and UDP service monitor showing counts of incoming and
outgoing packets for common TCP and UDP application ports, a LAN
statistics module that discovers active hosts and displays statistics
about their activity; TCP, UDP and other protocol display filters so
you can view just the traffic you want; logging; support for Ethernet,
FDDI, ISDN, SLIP, PPP, and loopback interfaces; and utilization of the
built-in raw socket interface of the Linux kernel, so it can be used
on a wide variety of supported network cards.

%description -l es.UTF-8
Herramienta para verificación de redes desde consolas.

%description -l pl.UTF-8
IPTraf jest narzędziem służącym do monitorowania sieci. Posiada
kolorowy, prosty w obsłudze interfejs. Współpracuje z wieloma
protokołami sieciowymi. Obsługuje standardy : Ethernet i PPP/SLIP.

%description -l pt_BR.UTF-8
O IPTraf é uma ferramenta de monitoração baseada no modo console, para
o Linux que mostra informações sobre o tráfego IP.

%description -l ru.UTF-8
IPTraf - консольная программа мониторинга сетевого IP-траффика. Ее
можно использовать, среди прочего, для определения типа траффика в
вашей сети и того, какой вид сервиса самый используемый на каких
компьютерах. IPTraf работает с интерфейсами Ethernet и SLIP/PPP.

%description -l uk.UTF-8
IPTraf - консольна утиліта моніторингу IP-трафіку в мережі. Її можна
використовувати, поміж іншим, для визначення типу трафіку у вашій
мережі і того, який вид сервісу найбільш використовується на
конкретних комп'ютерах. IPTraf працює з інтерфейсами Ethernet та
SLIP/PPP.

%define		_bindir		%{_sbindir}
%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	CPPFLAGS="-I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/{lib,log}/iptraf-ng

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ README* RELEASE*
%doc Documentation/*.{html,png}
%attr(755,root,root) %{_sbindir}/iptraf-ng
%attr(755,root,root) %{_sbindir}/rvnamed-ng
%attr(750,root,root) %dir /var/lib/iptraf-ng
%attr(750,root,root) %dir /var/log/iptraf-ng
%{_mandir}/man*/*
