# https://leetcode.com/problems/longest-palindromic-substring/

#https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
def get_string(S,Center,Radius):
    res=S[:Center-Radius]\
        +'<'\
        +S[Center-Radius:Center+Radius+1]\
        +'>'\
        +S[Center+Radius+1:]
    return res

def Longest_Palindrome(S):
    filler_char='#'
    # Transform the string S by inserting a bogus character ('#') between each character
    S_prime = filler_char + filler_char.join(S) + filler_char
    
    # The radius of the longest palindrome centered on each place in S'
    # note: length(S') = length(PalindromeRadii) = 2 * length(S) + 1
    PalindromeRadii = [0] * len(S_prime)
    
    Center = 0
    Radius = 0
    length_S_prime = len(S_prime)
    
    while Center < length_S_prime:
        # At the start of the loop, Radius is already set to a lower-bound
        # for the longest radius. In the first iteration, Radius is 0, but
        # it can be higher on later iterations.
        
        # Determine the longest palindrome starting at Center-Radius and
        # going to Center+Radius
        while Center - (Radius + 1) >= 0 and Center + (Radius + 1) < length_S_prime and S_prime[Center - (Radius + 1)] == S_prime[Center + (Radius + 1)]:
            Radius += 1
        
        # Save the radius of the longest palindrome in the array
        PalindromeRadii[Center] = Radius
        
        # Below, Center is incremented.
        # If any precomputed values can be reused, they are.
        # Also, Radius may be set to a value greater than 0
        OldCenter = Center
        OldRadius = Radius
        Center += 1

        # Radius' default value will be 0, if we reach the end of the
        # following loop.
        Radius = 0
        
        while Center <= OldCenter + OldRadius:
            # Because Center lies inside the old palindrome and every
            # character inside a palindrome has a "mirrored" character
            # reflected across its center, we can use the data that was
            # precomputed for the Center's mirrored point.
            
            MirroredCenter = OldCenter - (Center - OldCenter)
            MaxMirroredRadius = OldCenter + OldRadius - Center
            
            if PalindromeRadii[MirroredCenter] < MaxMirroredRadius:
                # The palindrome centered at MirroredCenter is entirely
                # contained in the palindrome centered at OldCenter
                # So, MirroredCenter and Center have the same sized palindrome
                print('*******************')
                print('PalindromeRadii[MirroredCenter] < MaxMirroredRadius')
                print('total')
                print(get_string(S_prime,OldCenter,OldRadius))
                print('left')
                print(get_string(S_prime,MirroredCenter,PalindromeRadii[MirroredCenter]))
                print('right')
                print(get_string(S_prime,Center,PalindromeRadii[MirroredCenter]))
                
                PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
                Center += 1
            elif PalindromeRadii[MirroredCenter] > MaxMirroredRadius:
                # The palindrome at MirroredCenter extends beyond the
                # palindrome at OldCenter. The palindrome at Center must
                # end at the edge of the OldCenter palindrome. Otherwise,
                # the palindrome at OldCenter would be bigger.
                print('*******************')
                print('PalindromeRadii[MirroredCenter] > MaxMirroredRadius')
                print('total')
                print(get_string(S_prime,OldCenter,OldRadius))
                print('left')
                print(get_string(S_prime,MirroredCenter,PalindromeRadii[MirroredCenter]))
                print('right')
                print(get_string(S_prime,Center,MaxMirroredRadius))
                PalindromeRadii[Center] = MaxMirroredRadius
                Center += 1
            else:  # PalindromeRadii[MirroredCenter] == MaxMirroredRadius
                print('*******************')
                print('PalindromeRadii[MirroredCenter] == MaxMirroredRadius')
                print('total')
                print(get_string(S_prime,OldCenter,OldRadius))
                print('left')
                print(get_string(S_prime,MirroredCenter,PalindromeRadii[MirroredCenter]))
                print('right')
                print(get_string(S_prime,Center,MaxMirroredRadius))
                # Since the palindrome at MirroredCenter ends exactly at
                # the edge of the palindrome centered at OldCenter, the
                # palindrome at Center might be bigger. Set Radius to the
                # minimum size of the palindrome at Center so it doesn't
                # recheck unnecessarily.
                
                Radius = MaxMirroredRadius
                break
    
    # A palindrome's size is equal to its radius * 2. However, since our
    # variable Radius considers our bogus characters to the side of the
    # center, the size of its corresponding palindrome is actually 2 *
    # (Radius / 2), which means a palindrome's size is equal to its
    # corresponding Radius value in PalindromeRadii
    
    max_radius = max(PalindromeRadii)
    center_index = PalindromeRadii.index(max_radius)
    
    # Determine the start index of the longest palindrome in the original string S
    start_index = (center_index - max_radius) // 2
    longest_palindrome_in_S = S[start_index:start_index + max_radius]
    
    return longest_palindrome_in_S

# Example usage
print(Longest_Palindrome("aabaabac"))  # Output: "aba" or "cdc" depending on the first longest palindrome found0