#include <iostream>
#include <algorithm>
#include <string>
#include <stdexcept>
#include <map>
#include <vector>
#include <list>

using namespace std;

auto sorted_word_counts(list < string > & words) {
  vector < pair < string, int >> v;
  map < string, int > counts;
  for (string word: words) {
    transform(word.begin(), word.end(), word.begin(), ::tolower);
    if (word != "") {
      counts[word]++;
    }
  }
  for (auto pair: counts) {
    v.push_back(make_pair(pair.first, pair.second));
  }
  sort(v.begin(), v.end(), [](auto x, auto y) {
    return x.second > y.second;
  });
  return v;
};

struct Sayer {
  string words;
  string operator()() {
    return words;
  }
  Sayer operator()(string word) {
    return {
      words + (words == "" ? "" : " ") + word
    };
  }
}
say;

template < typename T >

  class Queue {
    struct Node {
      T data;
      Node * next;
    };
    Node * tail = nullptr;
    Node * head = nullptr;
    int size = 0;
    
    public:
      ~Queue() {
        while (tail != nullptr) {
          dequeue();
        }
      }
    
    Queue() =
      default;
    Queue(const Queue & s) = delete;
    Queue & operator = (const Queue & s) = delete;
    Queue(Queue && s) {
      head = s.head;
      tail = s.tail;
      size = s.size;
      s.head = nullptr;
      s.tail = nullptr;
      s.size = 0;
    }
    
    Queue & operator = (Queue && s) {
      if ( & s != this) {
        size = s.size;
        head = s.head;
        tail = s.tail;
        s.head = nullptr;
        s.tail = nullptr;
        s.size = 0;
      }
      return *this;
    }
    
    int get_size() {
      return size;
    }
    
    T get_tail() {
      return tail -> data;
    }
    
    void enqueue(T x) {
      Node * newNode = new Node {
        x,
        nullptr
      };
      if (head == nullptr) {
        head = newNode;
      } else {
        tail -> next = newNode;
      }
      tail = newNode;
      size++;
    }
    
    T dequeue() {
      if (head == nullptr) {
        throw underflow_error("Can't dequeue an empty queue");
      }
      Node * nodeToDelete = head;
      T valueToReturn = head -> data;
      head = head -> next;
      size--;
      if (size == 0) {
        tail = nullptr;
      }
      delete nodeToDelete;
      return valueToReturn;
    }
    
  };
