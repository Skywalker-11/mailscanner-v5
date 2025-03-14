Name:               MailScanner
Version:            __Version__
Release:            __Release__.suse
Summary:            Email Gateway Virus Scanner with Malware, Phishing, and Spam Detection
Group:              System Environment/Daemons
License:            GPLv2
Vendor:             MailScanner Community
Packager:           MailScanner Team <https://www.mailscanner.info>
URL:                https://www.mailscanner.info
Requires:           perl >= 5.005
Provides:           perl(MailScanner), perl(MailScanner::Antiword), perl(MailScanner::BinHex), perl(MailScanner::Config), perl(MailScanner::ConfigSQL), perl(MailScanner::CustomConfig), perl(MailScanner::FileInto), perl(MailScanner::GenericSpam), perl(MailScanner::LinksDump), perl(MailScanner::Lock), perl(MailScanner::Log), perl(MailScanner::Mail), perl(MailScanner::MCP), perl(MailScanner::MCPMessage), perl(MailScanner::Message), perl(MailScanner::MessageBatch), perl(MailScanner::Quarantine), perl(MailScanner::Queue), perl(MailScanner::RBLs), perl(MailScanner::MCPMessage), perl(MailScanner::Message), perl(MailScanner::MCP), perl(MailScanner::SA), perl(MailScanner::Sendmail), perl(MailScanner::SMDiskStore), perl(MailScanner::SweepContent), perl(MailScanner::SweepOther), perl(MailScanner::SweepViruses), perl(MailScanner::TNEF), perl(MailScanner::Unzip), perl(MailScanner::WorkArea), perl(MIME::Parser::MailScanner)
Source:             %{name}-%{version}.tar.gz
BuildRoot:          %{_tmppath}/%{name}-root
BuildArchitectures: noarch
AutoReqProv:        no
Obsoletes:          mailscanner


%description
MailScanner is a freely distributable email gateway virus scanner with
malware, phishing, and spam detection. It supports Postfix, sendmail, 
ZMailer, Qmail or Exim mail transport agents and numerous open source 
and commercial virus scanning engines for virus scanning.  It will also 
selectively filter the content of email messages to protect users from 
offensive content such as pornographic spam. It also has features which 
protect it against Denial Of Service attacks.

After installation, you must install one of the supported open source or
commercial antivirus packages if not installed using the MailScanner
configuration script.

This has been tested on openSUSE Linux but should work on other SUSE
based Linux distributions.

%prep
%setup -q -n MailScanner-%{version}

%build

%install

mkdir -p $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/sbin/

while read f
do
  mkdir -p ${RPM_BUILD_ROOT}/etc/$f
done << EOF
MailScanner/conf.d
MailScanner/rules
MailScanner/mcp
cron.hourly
cron.daily
EOF

while read f
do
  mkdir -p ${RPM_BUILD_ROOT}/usr/share/$f
done << EOF
MailScanner/reports/hu
MailScanner/reports/de
MailScanner/reports/se
MailScanner/reports/ca
MailScanner/reports/cy+en
MailScanner/reports/pt_br
MailScanner/reports/fr
MailScanner/reports/es
MailScanner/reports/en
MailScanner/reports/en_uk
MailScanner/reports/cz
MailScanner/reports/it
MailScanner/reports/dk
MailScanner/reports/nl
MailScanner/reports/ro
MailScanner/reports/sk
MailScanner/perl/MailScanner
MailScanner/perl/custom
MailScanner/perl/Sendmail/PMilter
EOF

while read f
do
  mkdir -p ${RPM_BUILD_ROOT}/usr/lib/$f
done << EOF
MailScanner/wrapper
MailScanner/init
MailScanner/systemd
EOF

while read f
do
  mkdir -p ${RPM_BUILD_ROOT}/var/spool/MailScanner/$f
done << EOF
archive
incoming
quarantine
milterin
milterout
EOF

mkdir -p ${RPM_BUILD_ROOT}/usr/share/MailScanner/doc

### etc
install suse/etc/cron.daily/mailscanner ${RPM_BUILD_ROOT}/etc/cron.daily/
install suse/etc/cron.hourly/mailscanner ${RPM_BUILD_ROOT}/etc/cron.hourly/

### etc/MailScanner
install common/etc/MailScanner/conf.d/README ${RPM_BUILD_ROOT}/etc/MailScanner/conf.d/

while read f
do
  install common/etc/MailScanner/mcp/$f ${RPM_BUILD_ROOT}/etc/MailScanner/mcp/
done << EOF
10_example.cf
mcp.spamassassin.conf
EOF

while read f 
do
  install common/etc/MailScanner/rules/$f ${RPM_BUILD_ROOT}/etc/MailScanner/rules
done << EOF
bounce.rules
EXAMPLES
max.message.size.rules
README
spam.whitelist.rules
external.message.rules
EOF

while read f 
do
  install common/etc/MailScanner/$f ${RPM_BUILD_ROOT}/etc/MailScanner/
done << EOF
archives.filename.rules.conf
archives.filetype.rules.conf
country.domains.conf
defaults
filename.rules.conf
filetype.rules.conf
MailScanner.conf
phishing.bad.sites.conf
phishing.safe.sites.conf
spam.lists.conf
spamassassin.conf
virus.scanners.conf
EOF

### usr/sbin

install common/usr/sbin/MailScanner                        ${RPM_BUILD_ROOT}/usr/sbin/MailScanner
install common/usr/sbin/MSMilter                           ${RPM_BUILD_ROOT}/usr/sbin/MSMilter
install common/usr/sbin/ms-check                           ${RPM_BUILD_ROOT}/usr/sbin/ms-check
install common/usr/sbin/ms-clean-quarantine                ${RPM_BUILD_ROOT}/usr/sbin/ms-clean-quarantine
install common/usr/sbin/ms-create-locks                    ${RPM_BUILD_ROOT}/usr/sbin/ms-create-locks
install common/usr/sbin/ms-cron                            ${RPM_BUILD_ROOT}/usr/sbin/ms-cron
install common/usr/sbin/ms-d2mbox                          ${RPM_BUILD_ROOT}/usr/sbin/ms-d2mbox
install common/usr/sbin/ms-df2mbox                         ${RPM_BUILD_ROOT}/usr/sbin/ms-df2mbox
install common/usr/sbin/ms-msg-alert                       ${RPM_BUILD_ROOT}/usr/sbin/ms-msg-alert
install common/usr/sbin/ms-peek                            ${RPM_BUILD_ROOT}/usr/sbin/ms-peek
install common/usr/sbin/ms-perl-check                      ${RPM_BUILD_ROOT}/usr/sbin/ms-perl-check
install common/usr/sbin/ms-sa-cache                        ${RPM_BUILD_ROOT}/usr/sbin/ms-sa-cache
install common/usr/sbin/ms-update-bad-emails               ${RPM_BUILD_ROOT}/usr/sbin/ms-update-bad-emails
install common/usr/sbin/ms-update-phishing                 ${RPM_BUILD_ROOT}/usr/sbin/ms-update-phishing
install common/usr/sbin/ms-update-sa                       ${RPM_BUILD_ROOT}/usr/sbin/ms-update-sa
install common/usr/sbin/ms-update-vs                       ${RPM_BUILD_ROOT}/usr/sbin/ms-update-vs
install common/usr/sbin/ms-upgrade-conf                    ${RPM_BUILD_ROOT}/usr/sbin/ms-upgrade-conf
install suse/usr/sbin/ms-configure                         ${RPM_BUILD_ROOT}/usr/sbin/ms-configure

### usr/share/MailScanner

for lang in ca cy+en cz de dk en en_uk es fr hu it nl pt_br ro se sk
do
  while read f 
  do
    install common/usr/share/MailScanner/reports/$lang/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/reports/$lang
  done << EOF
deleted.content.message.txt
deleted.filename.message.txt
deleted.size.message.txt
deleted.virus.message.txt
disinfected.report.txt
inline.sig.html
inline.sig.txt
inline.spam.warning.txt
inline.warning.html
inline.warning.txt
inline.external.warning.html
inline.external.warning.txt
languages.conf
languages.conf.strings
recipient.mcp.report.txt
recipient.spam.report.txt
rejection.report.txt
sender.content.report.txt
sender.error.report.txt
sender.filename.report.txt
sender.mcp.report.txt
sender.size.report.txt
sender.spam.rbl.report.txt
sender.spam.report.txt
sender.spam.sa.report.txt
sender.virus.report.txt
stored.content.message.txt
stored.filename.message.txt
stored.size.message.txt
stored.virus.message.txt
EOF
done

install common/usr/share/MailScanner/perl/MailScanner.pm ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/

install common/usr/share/MailScanner/perl/Sendmail/Milter.pm ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/Sendmail/
install common/usr/share/MailScanner/perl/Sendmail/PMilter.pm ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/Sendmail/
install common/usr/share/MailScanner/perl/Sendmail/PMilter/Context.pm ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/Sendmail/PMilter

while read f 
do
  install common/usr/share/MailScanner/perl/MailScanner/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/MailScanner/
done << EOF
Antiword.pm
Config.pm
ConfigDefs.pl
ConfigSQL.pm
CustomConfig.pm
Exim.pm
EximDiskStore.pm
FileInto.pm
GenericSpam.pm
LinksDump.pm
Lock.pm
Log.pm
Mail.pm
MCP.pm
MCPMessage.pm
Message.pm
MessageBatch.pm
MSDiskStore.pm
MSMail.pm
PFDiskStore.pm
Postfix.pm
Qmail.pm
QMDiskStore.pm
Quarantine.pm
Queue.pm
RBLs.pm
SA.pm
Sendmail.pm
SMDiskStore.pm
SweepContent.pm
SweepOther.pm
SweepViruses.pm
SystemDefs.pm
TNEF.pm
Unzip.pm
WorkArea.pm
ZMailer.pm
ZMDiskStore.pm
EOF

while read f 
do
  install common/usr/share/MailScanner/perl/custom/$f ${RPM_BUILD_ROOT}/usr/share/MailScanner/perl/custom/
done << EOF
CustomAction.pm 
GenericSpamScanner.pm
LastSpam.pm
MyExample.pm
Ruleset-from-Function.pm
SpamWhitelist.pm
ZMRouterDirHash.pm
EOF

while read f
do 
  install $f ${RPM_BUILD_ROOT}/usr/share/MailScanner/doc/
done << EOF
changelog
README.md
LICENSE
EOF

### usr/lib/MailScanner

install common/usr/lib/MailScanner/init/ms-init ${RPM_BUILD_ROOT}/usr/lib/MailScanner/init/
install common/usr/lib/MailScanner/init/msmilter-init ${RPM_BUILD_ROOT}/usr/lib/MailScanner/init/
install common/usr/lib/MailScanner/systemd/ms-systemd ${RPM_BUILD_ROOT}/usr/lib/MailScanner/systemd/
install common/usr/lib/MailScanner/systemd/ms-milter ${RPM_BUILD_ROOT}/usr/lib/MailScanner/systemd/

while read f 
do
  install common/usr/lib/MailScanner/wrapper/$f ${RPM_BUILD_ROOT}/usr/lib/MailScanner/wrapper
done << EOF
avast-wrapper
avg-autoupdate
avg-wrapper
bitdefender-wrapper
bitdefender-autoupdate
clamav-autoupdate
clamav-wrapper
esets-wrapper
esets-wrapper-README
esetsefs-wrapper
esetsefs-wrapper-README
f-secure-wrapper
f-secure-autoupdate
f-secure-12-wrapper
generic-autoupdate
generic-wrapper
sophos-autoupdate
sophos-wrapper
drweb-wrapper
kaspersky-wrapper
EOF

MSVERSION=%{version}

perl -pi -e 's/VersionNumberHere/'$MSVERSION'/;' ${RPM_BUILD_ROOT}/etc/MailScanner/MailScanner.conf
perl -pi -e 's/VersionNumberHere/'$MSVERSION'/;' ${RPM_BUILD_ROOT}/usr/sbin/MailScanner

%clean
rm -rf ${RPM_BUILD_ROOT}

%pre

# back up their stuff
SAVEDIR="$HOME/ms_upgrade/saved.$$";

# remove old symlink if present
if [ -L '/etc/init.d/mailscanner' ]; then
    rm -f /etc/init.d/mailscanner
fi

# remove old file if present
if [ -f '/etc/init.d/mailscanner' ]; then
    rm -f /etc/init.d/mailscanner
fi

# remove old symlink if present
if [ -L '/etc/init.d/MailScanner' ]; then
    chkconfig --del MailScanner >/dev/null 2>&1
    rm -f /etc/init.d/MailScanner
fi

# remove old file if present
if [ -f '/etc/init.d/MailScanner' ]; then
    chkconfig --del MailScanner >/dev/null 2>&1
    rm -f /etc/init.d/MailScanner
fi

# remove old symlink if present
if [ -L '/etc/init.d/msmilter' ]; then
    chkconfig --del msmilter >/dev/null 2>&1
    rm -f /etc/init.d/msmilter
fi

# remove old file if present
if [ -f '/etc/init.d/msmilter' ]; then
    chkconfig --del msmilter >/dev/null 2>&1
    rm -f /etc/init.d/msmilter
fi

# remove systemd if present
if [ -f '/usr/lib/systemd/system/mailscanner.service' ]; then
    rm -f /usr/lib/systemd/system/mailscanner.service
fi

# remove systemd if present
if [ -f '/usr/lib/systemd/system/msmilter.service' ]; then
    rm -f /usr/lib/systemd/system/msmilter.service
fi

if [ -d '/usr/lib/MailScanner/MailScanner/CustomFunctions' ]; then
    mkdir -p ${SAVEDIR}/usr/lib/MailScanner/MailScanner/CustomFunctions
    cp -f /usr/lib/MailScanner/MailScanner/CustomFunctions/* ${SAVEDIR}/usr/lib/MailScanner/MailScanner/CustomFunctions
    if [ -d "/usr/lib/MailScanner/MailScanner" ]; then
        rm -rf /usr/lib/MailScanner/MailScanner
    fi
fi

if [ -d '/etc/MailScanner/CustomFunctions' ]; then
    mkdir -p ${SAVEDIR}/etc/MailScanner/CustomFunctions
    cp -f /etc/MailScanner/CustomFunctions/* ${SAVEDIR}/etc/MailScanner/CustomFunctions
    rm -rf /etc/MailScanner/CustomFunctions
fi

if [ -L '/etc/MailScanner/CustomFunctions' ]; then
    rm -f /etc/MailScanner/CustomFunctions
fi

if [ -f '/etc/MailScanner/CustomConfig.pm' ]; then
    mkdir -p ${SAVEDIR}/etc/MailScanner
    cp -f /etc/MailScanner/CustomConfig.pm ${SAVEDIR}/etc/MailScanner/
    rm -f /etc/MailScanner/CustomConfig.pm
fi

if [ -d '/etc/MailScanner/reports' ]; then
    mkdir -p ${SAVEDIR}/etc/MailScanner/reports
    cp -rf /etc/MailScanner/reports/* ${SAVEDIR}/etc/MailScanner/reports
    rm -rf /etc/MailScanner/reports
fi

if [ -d '/usr/share/MailScanner/MailScanner' ]; then
    rm -rf /usr/share/MailScanner/MailScanner
fi

if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
    mkdir -p ${SAVEDIR}/etc/MailScanner
    cp -f /etc/MailScanner/MailScanner.conf ${SAVEDIR}/etc/MailScanner/MailScanner.conf.original
    cp -f /etc/MailScanner/MailScanner.conf /etc/MailScanner/MailScanner.conf.original
fi

exit 0

%post

# back up their stuff
SAVEDIR="$HOME/ms_upgrade/saved.$$";

if [ ! -d '/var/spool/MailScanner/archive' ]; then
    mkdir -p /var/spool/MailScanner/archive
    chmod 775 /var/spool/MailScanner/archive
fi

# group for users to run under
if ! getent group mtagroup >/dev/null 2>&1; then
    groupadd -f mtagroup >/dev/null 2>&1
fi

if [ $(stat -c "%G" /var/spool/MailScanner/archive) == 'root' ]; then
    chgrp mtagroup /var/spool/MailScanner/archive
fi

if [ ! -d '/var/spool/MailScanner/incoming' ]; then
    mkdir -p /var/spool/MailScanner/incoming
    chmod 775 /var/spool/MailScanner/incoming
fi

if [ $(stat -c "%G" /var/spool/MailScanner/incoming) == 'root' ]; then
    chgrp mtagroup /var/spool/MailScanner/incoming
fi

if [ ! -d '/var/spool/MailScanner/quarantine' ]; then
    mkdir -p /var/spool/MailScanner/quarantine
    chmod 775 /var/spool/MailScanner/quarantine
fi

if [ $(stat -c "%G" /var/spool/MailScanner/quarantine) == 'root' ]; then
    chgrp mtagroup /var/spool/MailScanner/quarantine
fi

if [ ! -d '/var/spool/MailScanner/milterin' ]; then
    mkdir -p /var/spool/MailScanner/milterin
    chmod 775 /var/spool/MailScanner/milterin
fi

if [ $(stat -c "%G" /var/spool/MailScanner/milterin) == 'root' ]; then
    chgrp mtagroup /var/spool/MailScanner/milterin
fi

if [ ! -d '/var/spool/MailScanner/milterout' ]; then
    mkdir -p /var/spool/MailScanner/milterout
    chmod 775 /var/spool/MailScanner/milterout
fi

if [ $(stat -c "%G" /var/spool/MailScanner/milterout) == 'root' ]; then
    chgrp mtagroup /var/spool/MailScanner/milterout
fi

if [ -f '/etc/MailScanner/spam.assassin.prefs.conf' ]; then
    mv -f /etc/MailScanner/spam.assassin.prefs.conf /etc/MailScanner/spamassassin.conf
fi

# remove old link if present
if [ -L '/etc/mail/spamassassin/mailscanner.cf' ]; then
    rm -f /etc/mail/spamassassin/mailscanner.cf
fi

if [ -L '/etc/mail/spamassassin/MailScanner.cf' ]; then
    rm -f /etc/mail/spamassassin/MailScanner.cf
fi

if [ -f '/etc/MailScanner/spam.assassin.prefs.conf' ]; then
    mv -f /etc/MailScanner/spam.assassin.prefs.conf /etc/MailScanner/spamassassin.conf
fi

# upgrade the old config
if [ -f /etc/MailScanner/MailScanner.conf.original -a -f /etc/MailScanner/MailScanner.conf ]; then
    cp -f /etc/MailScanner/MailScanner.conf /etc/MailScanner/MailScanner.conf.dist
    ms-upgrade-conf /etc/MailScanner/MailScanner.conf.original /etc/MailScanner/MailScanner.conf.dist > /etc/MailScanner/MailScanner.conf
    mkdir -p ${SAVEDIR}/etc/MailScanner
    mv -f /etc/MailScanner/MailScanner.conf.* ${SAVEDIR}/etc/MailScanner > /dev/null 2>&1
    cp -f /etc/MailScanner/MailScanner.conf ${SAVEDIR}/etc/MailScanner/MailScanner.new > /dev/null 2>&1
fi

# update web bug link
OLD="^Web Bug Replacement.*";
NEW="Web Bug Replacement = data:image\/gif;base64,R0lGODlhAQABAJEAAP\/\/\/wAAAAAAAAAAACH5BAkAAAAALAAAAAABAAEAAAgEAAEEBAA7";
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
    sed -i "s/${OLD}/${NEW}/g" /etc/MailScanner/MailScanner.conf
fi

# fix reports directory
OLDTHING='\/etc\/MailScanner\/reports';
NEWTHING='\/usr\/share\/MailScanner\/reports';
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
    sed -i "s/${OLDTHING}/${NEWTHING}/g" /etc/MailScanner/MailScanner.conf
fi

# fix custom functions directory
OLDTHING='^Custom Functions Dir.*';
NEWTHING='Custom Functions Dir = \/usr\/share\/MailScanner\/perl\/custom';
if [ -f '/etc/MailScanner/MailScanner.conf' ]; then
    sed -i "s/${OLDTHING}/${NEWTHING}/g" /etc/MailScanner/MailScanner.conf
fi

# softlink for custom functions
if [ -d '/usr/share/MailScanner/perl/custom' -a ! -L '/etc/MailScanner/custom' ]; then
    ln -s /usr/share/MailScanner/perl/custom/ /etc/MailScanner/custom
fi

# softlink for custom reports
if [ -d '/usr/share/MailScanner/reports' -a ! -L '/etc/MailScanner/reports' ]; then
    ln -s /usr/share/MailScanner/reports /etc/MailScanner/reports
fi

# Check for systemd
if [ -f '/lib/systemd/systemd' -o -f '/usr/lib/systemd/systemd' ]; then
    cp /usr/lib/MailScanner/systemd/ms-systemd /usr/lib/systemd/system/mailscanner.service
    cp /usr/lib/MailScanner/systemd/ms-milter /usr/lib/systemd/system/msmilter.service
# create init.d symlink
elif [ -d '/etc/init.d' -a ! -L '/etc/init.d/mailscanner' -a -f '/usr/lib/MailScanner/init/ms-init' ]; then
    ln -s /usr/lib/MailScanner/init/ms-init /etc/init.d/mailscanner
    # Sort out the rc.d directories
    chkconfig --list mailscanner >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        chkconfig --add mailscanner
        chkconfig mailscanner off
    fi
    ln -s /usr/lib/MailScanner/init/msmilter-init /etc/init.d/msmilter
    # Sort out the rc.d directories
    chkconfig --list msmilter >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        chkconfig --add msmilter
        chkconfig msmilter off
    fi
fi

echo
echo To initially configure MailScanner and install necessary modules run:
echo 
echo /usr/sbin/ms-configure
echo
echo To update MailScanner and necessary modules run:
echo 
echo /usr/sbin/ms-configure --update
echo

%preun
if [ $1 = 0 ]; then
    # We are being deleted, not upgraded
    if [ -f '/usr/lib/systemd/systemd' ]; then
        systemctl stop mailscanner.service >/dev/null 2>&1
        systemctl disable mailscanner.service
        rm -f /usr/lib/systemd/system/mailscanner.service
        systemctl stop msmilter.service >/dev/null 2>&1
        systemctl disable msmilter.service >/dev/null 2>&1
    else
        service mailscanner stop >/dev/null 2>&1
        chkconfig mailscanner off
        chkconfig --del mailscanner
        service msmilter stop >/dev/null 2>&1
        chkconfig msmilter off
        chkconfig --del msmilter
    fi
fi
exit 0

%postun
# delete old ms files if this is an upgrade
if [ -d '/var/lib/MailScanner' ]; then
    rm -rf /var/lib/MailScanner
fi
exit 0

%files
%defattr (644,root,root)
%attr(755,root,root) %dir /etc/MailScanner
%attr(755,root,root) %dir /etc/MailScanner/rules
%attr(755,root,root) %dir /etc/MailScanner/mcp
%attr(755,root,root) %dir /etc/MailScanner/conf.d
%attr(755,root,root) %dir /usr/lib/MailScanner/wrapper
%attr(755,root,root) %dir /usr/lib/MailScanner/init
%attr(755,root,root) %dir /usr/lib/MailScanner/systemd
%attr(755,root,root) %dir /usr/share/MailScanner
%attr(755,root,root) %dir /usr/share/MailScanner/doc
%attr(755,root,root) %dir /usr/share/MailScanner/perl
%attr(755,root,root) %dir /usr/share/MailScanner/perl/custom
%attr(755,root,root) %dir /usr/share/MailScanner/perl/MailScanner
%attr(755,root,root) %dir /usr/share/MailScanner/reports
%attr(775,root,root) %dir /var/spool/MailScanner/archive
%attr(775,root,root) %dir /var/spool/MailScanner/incoming
%attr(775,root,root) %dir /var/spool/MailScanner/milterin
%attr(775,root,root) %dir /var/spool/MailScanner/milterout
%attr(775,root,root) %dir /var/spool/MailScanner/quarantine

%attr(755,root,root) /usr/sbin/MailScanner
%attr(755,root,root) /usr/sbin/MSMilter
%attr(755,root,root) /usr/sbin/ms-check
%attr(755,root,root) /usr/sbin/ms-clean-quarantine
%attr(755,root,root) /usr/sbin/ms-create-locks
%attr(755,root,root) /usr/sbin/ms-cron
%attr(755,root,root) /usr/sbin/ms-d2mbox
%attr(755,root,root) /usr/sbin/ms-df2mbox
%attr(755,root,root) /usr/sbin/ms-msg-alert
%attr(755,root,root) /usr/sbin/ms-peek
%attr(755,root,root) /usr/sbin/ms-perl-check
%attr(755,root,root) /usr/sbin/ms-sa-cache
%attr(755,root,root) /usr/sbin/ms-update-bad-emails
%attr(755,root,root) /usr/sbin/ms-update-phishing
%attr(755,root,root) /usr/sbin/ms-update-sa
%attr(755,root,root) /usr/sbin/ms-update-vs
%attr(755,root,root) /usr/sbin/ms-upgrade-conf
%attr(755,root,root) /usr/sbin/ms-configure

%attr(755,root,root) /usr/lib/MailScanner/init/ms-init
%attr(755,root,root) /usr/lib/MailScanner/init/msmilter-init
%attr(644,root,root) /usr/lib/MailScanner/systemd/ms-systemd
%attr(644,root,root) /usr/lib/MailScanner/systemd/ms-milter

%attr(755,root,root) /usr/lib/MailScanner/wrapper/avast-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/avg-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/avg-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/bitdefender-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/bitdefender-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/clamav-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/clamav-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/esets-wrapper
%attr(644,root,root) /usr/lib/MailScanner/wrapper/esets-wrapper-README
%attr(755,root,root) /usr/lib/MailScanner/wrapper/esetsefs-wrapper
%attr(644,root,root) /usr/lib/MailScanner/wrapper/esetsefs-wrapper-README
%attr(755,root,root) /usr/lib/MailScanner/wrapper/f-secure-12-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/f-secure-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/f-secure-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/generic-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/generic-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/sophos-autoupdate
%attr(755,root,root) /usr/lib/MailScanner/wrapper/sophos-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/drweb-wrapper
%attr(755,root,root) /usr/lib/MailScanner/wrapper/kaspersky-wrapper

%config(noreplace) /usr/share/MailScanner/perl/custom/CustomAction.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/GenericSpamScanner.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/LastSpam.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/MyExample.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/Ruleset-from-Function.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/SpamWhitelist.pm
%config(noreplace) /usr/share/MailScanner/perl/custom/ZMRouterDirHash.pm

%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Antiword.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Config.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ConfigDefs.pl
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ConfigSQL.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/CustomConfig.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Exim.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/EximDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/FileInto.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/GenericSpam.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/LinksDump.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Lock.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Log.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Mail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MCP.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MCPMessage.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Message.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MessageBatch.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MSDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/MSMail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/PFDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Postfix.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Qmail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/QMDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Quarantine.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Queue.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/RBLs.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SA.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Sendmail.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SMDiskStore.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepContent.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepOther.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SweepViruses.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/SystemDefs.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/TNEF.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/Unzip.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/WorkArea.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ZMailer.pm
%attr(644,root,root) /usr/share/MailScanner/perl/MailScanner/ZMDiskStore.pm

%attr(644,root,root) /usr/share/MailScanner/perl/Sendmail/Milter.pm
%attr(644,root,root) /usr/share/MailScanner/perl/Sendmail/PMilter.pm
%attr(644,root,root) /usr/share/MailScanner/perl/Sendmail/PMilter/Context.pm

%attr(755,root,root) /etc/cron.daily/mailscanner
%attr(755,root,root) /etc/cron.hourly/mailscanner

%config(noreplace) /etc/MailScanner/archives.filename.rules.conf
%config(noreplace) /etc/MailScanner/archives.filetype.rules.conf
%attr(644,root,root) /etc/MailScanner/country.domains.conf
%config(noreplace) /etc/MailScanner/defaults
%config(noreplace) /etc/MailScanner/filename.rules.conf
%config(noreplace) /etc/MailScanner/filetype.rules.conf
%attr(644,root,root) /etc/MailScanner/MailScanner.conf
%attr(644,root,root) /etc/MailScanner/phishing.safe.sites.conf
%attr(644,root,root) /etc/MailScanner/phishing.bad.sites.conf
%attr(644,root,root) /etc/MailScanner/spam.lists.conf
%config(noreplace) /etc/MailScanner/spamassassin.conf
%attr(644,root,root) /etc/MailScanner/virus.scanners.conf

%attr(644,root,root) /etc/MailScanner/conf.d/README

%config(noreplace) /etc/MailScanner/mcp/10_example.cf
%config(noreplace) /etc/MailScanner/mcp/mcp.spamassassin.conf

%config(noreplace) /etc/MailScanner/rules/bounce.rules
%attr(644,root,root) /etc/MailScanner/rules/EXAMPLES
%config(noreplace) /etc/MailScanner/rules/max.message.size.rules
%attr(644,root,root) /etc/MailScanner/rules/README
%config(noreplace) /etc/MailScanner/rules/spam.whitelist.rules
%config(noreplace) /etc/MailScanner/rules/external.message.rules

%attr(644,root,root) /usr/share/MailScanner/doc/changelog
%attr(644,root,root) /usr/share/MailScanner/doc/LICENSE
%attr(644,root,root) /usr/share/MailScanner/doc/README.md

%config(noreplace) /usr/share/MailScanner/reports/en/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/en/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/en/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/en/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/en/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/en/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/en_uk/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/en_uk/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/en_uk/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/en_uk/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cy+en/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/cy+en/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/cy+en/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cy+en/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/de/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/de/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/de/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/de/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/de/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/de/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/de/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/de/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/fr/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/fr/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/fr/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/fr/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/es/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/es/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/es/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/es/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/es/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/es/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/es/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/es/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/nl/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/nl/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/nl/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/nl/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/pt_br/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/pt_br/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/pt_br/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/pt_br/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/sk/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/sk/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/sk/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/sk/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/dk/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/dk/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/dk/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/dk/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/it/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/it/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/it/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/it/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/it/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/it/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/it/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/it/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ro/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/ro/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/ro/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ro/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/se/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/se/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/se/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/se/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/se/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/se/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/se/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/se/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/cz/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/cz/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/cz/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/cz/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/hu/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/hu/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/hu/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/hu/stored.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.content.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.content.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/deleted.virus.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/disinfected.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.sig.html
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.sig.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.spam.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.external.warning.html
%config(noreplace) /usr/share/MailScanner/reports/ca/inline.external.warning.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/languages.conf
%config(noreplace) /usr/share/MailScanner/reports/ca/languages.conf.strings
%config(noreplace) /usr/share/MailScanner/reports/ca/recipient.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/recipient.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/rejection.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.error.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.filename.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.rbl.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.spam.sa.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.mcp.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.size.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/sender.virus.report.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.filename.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.size.message.txt
%config(noreplace) /usr/share/MailScanner/reports/ca/stored.virus.message.txt

%changelog
* Sat Oct 29 2022 Shawn Iverson <shawniverson@efa-project.org>
- Integrate working PMilter code into MailScanner

* Sat Jan 08 2022 Shawn Iverson <shawniverson@efa-project.org>
- Revert addition of 1x1spacer.gif in favor of base64 embedding

* Tue Jan 04 2022 Shawn Iverson <shawniverson@efa-project.org>
- Remove 1x1spacer.gif default hosted url

* Sat May 16 2020 Shawn Iverson <shawniverson@efa-project.org>
- Refactor to simplify build and spec

* Sat Nov 02 2019 Shawn Iverson <shawniverson@efa-project.org>
- Refactor for standard package management

* Sun Jul 07 2019 Shawn Iverson <shawniverson@efa-project.org>
- Add back directories to files section and test group membership

* Sun Jul 07 2019 Shawn Iverson <shawniverson@efa-project.org>
- Add external inline message files and rules

* Sun Jun 30 2019 Shawn Iverson <shawniverson@efa-project.org>
- Create and set permissions and ownership during post as needed

* Tue Feb 26 2019 Shawn Iverson <shawniverson@efa-project.org>
- Add esets-wrapper-README

* Sun Oct 21 2018 Shawn Iverson <shawniverson@efa-project.org>
- Add en_uk reports and drweb-wrapper

* Sat Oct 20 2018 Shawn Iverson <shawniverson@efa-project.org>
- Add kaspersky-wrapper

* Sat Aug 25 2018 Shawn Iverson <shawniverson@gmail.com>
- Add Milter support for MailScanner

* Sun Sep 03 2017 Shawn Iverson <shawniverson@gmail.com>
- Preserve quarantine perms and better init runlevel handling

* Sun Aug 27 2017 Shawn Iverson <shawniverson@gmail.com>
- Remove execute bit on systemd script

* Sat Aug 19 2017 Shawn Iverson <shawniverson@gmail.com>
- ms-update-phishing

* Mon Jul 24 2017 Shawn Iverson <shawniverson@gmail.com>
- Better detection of systemd

* Sun May 28 2017 Shawn Iverson <shawniverson@gmail.com>
- mailscanner systemd support for SuSE Linux

* Thu Nov 10 2016 Jerry Benton <mailscanner@mailborder.com>
- see https://github.com/MailScanner/v5/blob/master/changelog

* Sat Apr 30 2016 Jerry Benton <mailscanner@mailborder.com>
- v5 initial release

