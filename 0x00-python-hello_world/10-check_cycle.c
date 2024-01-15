#include "list.h"

/**
 * check_cycle - check if linked list has a cycle
 *
 * list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle and 1 if there is cycle
 */
int check_cycle(listint_t *list) {
  listint_t *fast, *slow;

  if (!list)
    return 0;
  fast = slow = list;
  while (fast->next && fast->next->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast)
      return 1;
  }
  return 0;
}
