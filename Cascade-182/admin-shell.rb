#!/usr/bin/ruby
require 'winrm'

conn = WinRM::Connection.new(
  endpoint: 'http://10.10.10.182:5985/wsman',
  user: 'Administrator',
  password: 'baCT3r1aN00dles',
)

command=""

conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        print "PS > "
        command = gets
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end
    puts "Exiting with code #{output.exitcode}"
end
