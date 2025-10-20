class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            print("Heap is empty.")
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            print("Heap is empty. Cannot remove.")
            return None
        min_patient = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return min_patient


# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.insert(Patient("Morgan", 2))
heap.insert(Patient("Casey", 1))  # Duplicate urgency

heap.print_heap()
# Expected order: Taylor (1), Casey (1), Morgan (2), Jordan (3), Avery (5)

print("\nPeek at next patient:")
next_up = heap.peek()
if next_up:
    print(next_up.name, next_up.urgency)  # Should be Taylor or Casey (urgency 1)

print("\nRemoving patients:")
while heap.data:
    served = heap.remove_min()
    print(f"Served: {served.name} ({served.urgency})")

# Edge case: removing from empty heap
print("\nAttempting to remove from empty heap:")
heap.remove_min()  # Should print error message

# Edge case: peeking into empty heap
print("\nAttempting to peek into empty heap:")
heap.peek()  # Should print error message

# Design Memo

#The emergency_queue.py file models an emergency intake system using a min-heap. 
#This is a smart way to manage patients based on urgency because it always keeps the most critical patient at the top of the queue. 
#The Patient class stores each patient's name and urgency level, where a lower number means higher priority. 
#The MinHeap class manages the queue and uses helper methods to keep the heap organized.
#When a new patient is added, the heapify_up method checks if they need to move up the queue based on urgency. 
#If a patient is removed, heapify_down makes sure the next most urgent patient moves to the top. 
#These methods help maintain the heap structure and make sure the system responds quickly to changes. 
#The heap also supports methods like insert, peek, remove_min, and print_heap, which make it easy to manage and view the queue.
#This kind of system is useful in real-world settings like hospitals, customer service, or task scheduling. 
#It ensures that the most important cases are handled first, even as new ones arrive. 
#The design also handles edge cases like removing from an empty heap or inserting patients with the same urgency level.
#Using a heap for this problem shows how data structures can improve decision-making and efficiency. 
#It supports fast access and updates, which are important in time-sensitive situations. 
#The implementation also helps reinforce key programming skills like class design, list manipulation, and algorithm development.
#In summary, the min-heap is a great choice for managing urgency-based workflows. 
#It is simple, fast, and reliable, making it ideal for systems that need to prioritize tasks or people in real time.
